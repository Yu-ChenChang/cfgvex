## Needs make version higher than 4 ##
BINDIR32 = ../x86
BINDIR64 = ../x86_64
SRCS = $(wildcard *.c)
bns = $(basename $(SRCS))

o-objs=$(addsuffix $(O), $(m-objs))
targets=$(addsuffix .o, $(o-objs))

all:$(targets)

compilers=gcc clang
archs=-m32 -m64
opts=-O0 -O1 -O2 -O3 -Os

define build_template =
ifeq ($(3),-m32)
all:$(BINDIR32)/$(1)-$(2)$(3)$(4).o 
$(BINDIR32)/$(1)-$(2)$(3)$(4).o:$(1).c
ifeq ($(2),clang)
	clang -g -m32 $(4) -c $(1).c -o $(BINDIR32)/$(1)-$(2)$(3)$(4).o
else  # gcc
	gcc -g -m32 $(4) -c $(1).c -o $(BINDIR32)/$(1)-$(2)$(3)$(4).o
endif
else # -m64
all:$(BINDIR64)/$(1)-$(2)$(3)$(4).o
$(BINDIR64)/$(1)-$(2)$(3)$(4).o:$(1).c
ifeq ($(2),clang)
	clang -g -m64 $(4) -c $(1).c -o $(BINDIR64)/$(1)-$(2)$(3)$(4).o
else  # gcc
	gcc -g -m64 $(4) -c $(1).c -o $(BINDIR64)/$(1)-$(2)$(3)$(4).o
endif
endif
endef

$(foreach f,$(bns), $(foreach c,$(compilers),$(foreach a,$(archs), $(foreach o,$(opts),$(eval $(call build_template,$(f),$(c),$(a),$(o)))))))

%.o:%.c
	$(CC) -c $(O) $(ARCH) $<

clean:
	rm -f *.o
