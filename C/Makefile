COMPILER=gcc
SRCS:=$(filter-out testsuite.c, $(wildcard *.c))
OBJS:=$(patsubst %.c, %.o, $(SRCS)) 

build: $(SRCS)
	$(COMPILER) -o math.o -c math.c

analyse: $(SRCS)
	cppcheck --error-exitcode=1 .

testsuite: build testsuite.c
	$(COMPILER) $(OBJS) testsuite.c -lcunit -o $@
	./$@
