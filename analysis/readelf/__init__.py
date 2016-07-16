
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

	def get_func_with_params(self):
		""" Dump the debugging info section.
		"""
		self._init_dwarfinfo()
		if self._dwarfinfo is None:
			return
		section_offset = self._dwarfinfo.debug_info_sec.global_offset
		# Offset of the .debug_info section in the stream
		for cu in self._dwarfinfo.iter_CUs():
			funcDic = {} 
			paraCount = 0
			funcName=""
			for die in cu.iter_DIEs():
				if die.tag == 'DW_TAG_subprogram':
					if funcName != "":
						funcDic[funcName] = paraCount
						paraCount=0
					for i,attr in enumerate(itervalues(die.attributes)):
						if i==1:
							funcName=describe_attr_value(attr, die, section_offset).split()[-1]

				elif die.tag == 'DW_TAG_formal_parameter':
					paraCount+=1
			if funcName != "":
				funcDic[funcName] = paraCount
		for ele in funcDic:
			print '%s: %d' % (
				ele,
				funcDic[ele]
				)
		return funcDic
def program_dwarf(pName):
	with open(pName, 'rb') as file:
		try:
			readelf = ReadElf(file, sys.stdout)
			funcDic = readelf.get_func_with_params()
		except ELFError as ex:
			sys.stderr.write('ELF error: %s\n' % ex)
			sys.exit(1)

if __name__ == '__main__':
	program_dwarf('../../testcases/c_func_test/src/simple_c_func_test')
