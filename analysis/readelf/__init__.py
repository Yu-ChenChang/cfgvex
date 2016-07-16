
import os, sys
import string
sys.path.insert(0, '.')


from elftools import __version__
from elftools.common.exceptions import ELFError
from elftools.common.py3compat import (
		ifilter, byte2int, bytes2str, itervalues, str2bytes)
from elftools.elf.elffile import ELFFile
from elftools.elf.dynamic import DynamicSection, DynamicSegment
from elftools.elf.enums import ENUM_D_TAG
from elftools.elf.segments import InterpSegment, NoteSegment
from elftools.elf.sections import SymbolTableSection
from elftools.elf.gnuversions import (
	GNUVerSymSection, GNUVerDefSection,
	GNUVerNeedSection,
	)
from elftools.elf.relocation import RelocationSection
from elftools.elf.descriptions import (
	describe_ei_class, describe_ei_data, describe_ei_version,
	describe_ei_osabi, describe_e_type, describe_e_machine,
	describe_e_version_numeric, describe_p_type, describe_p_flags,
	describe_sh_type, describe_sh_flags,
	describe_symbol_type, describe_symbol_bind, describe_symbol_visibility,
	describe_symbol_shndx, describe_reloc_type, describe_dyn_tag,
	describe_ver_flags, describe_note
	)
from elftools.elf.constants import E_FLAGS
from elftools.dwarf.dwarfinfo import DWARFInfo
from elftools.dwarf.descriptions import (
	describe_reg_name, describe_attr_value, set_global_machine_arch,
	describe_CFI_instructions, describe_CFI_register_rule,
	describe_CFI_CFA_rule,
	)
from elftools.dwarf.constants import (
	DW_LNS_copy, DW_LNS_set_file, DW_LNE_define_file)
from elftools.dwarf.callframe import CIE, FDE

class ReadElf(object):
	""" display_* methods are used to emit output into the output stream
	"""
	def __init__(self, file, output):
		""" file:
				stream object with the ELF file to read

			output:
				output stream to write to
		"""
		self.elffile = ELFFile(file)
		self.output = output

		# Lazily initialized if a debug dump is requested
		self._dwarfinfo = None

		self._versioninfo = None

	def _init_dwarfinfo(self):
		""" Initialize the DWARF info contained in the file and assign it to
			self._dwarfinfo.
			Leave self._dwarfinfo at None if no DWARF info was found in the file
		"""
		if self._dwarfinfo is not None:
			return

		if self.elffile.has_dwarf_info():
			self._dwarfinfo = self.elffile.get_dwarf_info()
		else:
			self._dwarfinfo = None

	def display_debug_dump(self):
		""" Dump the debugging info section.
		"""
		self._init_dwarfinfo()
		if self._dwarfinfo is None:
			return
		section_offset = self._dwarfinfo.debug_info_sec.global_offset
		# Offset of the .debug_info section in the stream
		for cu in self._dwarfinfo.iter_CUs():
			self._emitline('  Compilation Unit @ offset %s:' %
				self._format_hex(cu.cu_offset))
			self._emitline('   Length:		  %s (%s)' % (
				self._format_hex(cu['unit_length']),
				'%s-bit' % cu.dwarf_format()))
			self._emitline('   Version:		  %s' % cu['version']),
			self._emitline('   Abbrev Offset: %s' % (
				self._format_hex(cu['debug_abbrev_offset']))),
			self._emitline('   Pointer Size:  %s' % cu['address_size'])

			# The nesting depth of each DIE within the tree of DIEs must be
			# displayed. To implement this, a counter is incremented each time
			# the current DIE has children, and decremented when a null die is
			# encountered. Due to the way the DIE tree is serialized, this will
			# correctly reflect the nesting depth
			#
			die_depth = 0
			for die in cu.iter_DIEs():
				self._emitline(' <%s><%x>: Abbrev Number: %s%s' % (
					die_depth,
					die.offset,
					die.abbrev_code,
					(' (%s)' % die.tag) if not die.is_null() else ''))
				if die.is_null():
					die_depth -= 1
					continue

				for attr in itervalues(die.attributes):
					name = attr.name
					# Unknown attribute values are passed-through as integers
					if isinstance(name, int):
						name = 'Unknown AT value: %x' % name
					self._emitline('	<%x>   %-18s: %s' % (
						attr.offset,
						name,
						describe_attr_value(
							attr, die, section_offset)))

				if die.has_children:
					die_depth += 1

		self._emitline()

	def _format_hex(self, addr, fieldsize=None, fullhex=False, lead0x=True,
					alternate=False):
		""" Format an address into a hexadecimal string.

			fieldsize:
				Size of the hexadecimal field (with leading zeros to fit the
				address into. For example with fieldsize=8, the format will
				be %08x
				If None, the minimal required field size will be used.

			fullhex:
				If True, override fieldsize to set it to the maximal size
				needed for the elfclass

			lead0x:
				If True, leading 0x is added

			alternate:
				If True, override lead0x to emulate the alternate
				hexadecimal form specified in format string with the #
				character: only non-zero values are prefixed with 0x.
				This form is used by readelf.
		"""
		if alternate:
			if addr == 0:
				lead0x = False
			else:
				lead0x = True
				fieldsize -= 2

		s = '0x' if lead0x else ''
		if fullhex:
			fieldsize = 8 if self.elffile.elfclass == 32 else 16
		if fieldsize is None:
			field = '%x'
		else:
			field = '%' + '0%sx' % fieldsize
		return s + field % addr

	def _emitline(self, s=''):
		""" Emit an object to output, followed by a newline
		"""
		self.output.write(str(s).rstrip() + '\n')
def program_dwarf(pName):
	with open(pName, 'rb') as file:
		try:
			readelf = ReadElf(file, sys.stdout)
			readelf.display_debug_dump()
		except ELFError as ex:
			sys.stderr.write('ELF error: %s\n' % ex)
			sys.exit(1)

if __name__ == '__main__':
	program_dwarf('../../testcases/c_func_test/src/simple_c_func_test')
