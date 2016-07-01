SRCS = $(wildcard *.c)
bns = $(basename $(SRCS))

# o-objs=$(addsuffix $(O), $(m-objs))
# targets=$(addsuffix .o, $(o-objs))

# all:$(targets)

compilers=gcc clang
archs=-m32 -m64
opts=-O0 -O1 -O2 -O3 -Os

define build_template =
all:$(1)-$(2)$(3)$(4).o
$(1)-$(2)$(3)$(4).o:$(1).c
ifeq ($(2),clang)
ifeq ($(3),-m32)
	clang -m32 $(4) -c $(1).c -o $(1)-$(2)$(3)$(4).o
else
	clang -m64 $(4) -c $(1).c -o $(1)-$(2)$(3)$(4).o
endif
else  # gcc
ifeq ($(3),-m32)
	gcc -m32 $(4) -c $(1).c -o $(1)-$(2)$(3)$(4).o
else
	gcc -m64 $(4) -c $(1).c -o $(1)-$(2)$(3)$(4).o
endif
endif
endef

$(foreach f,$(bns), $(foreach c,$(compilers),$(foreach a,$(archs), $(foreach o,$(opts),$(eval $(call build_template,$(f),$(c),$(a),$(o)))))))

%.o:%.c
	$(CC) -c $(O) $(ARCH) $<

clean:
	rm -f *.o
