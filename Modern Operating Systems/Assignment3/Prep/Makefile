#This target will compile all the files mentioned

#3 object files for 3 cpp files
all: hello

#3 dependencies, target is hello (in turn "all")
hello: main.o function1.o function2.o
	g++ main.o function1.o function2.o -o hello 
#command

#after colon with space is called dependency, if Dependency is satisfied then command is executed
#Target: Dependency

main.o: main.cpp
	g++ -c main.cpp 

#Command
#execute this -c = compile

function1.o: function1.cpp
	g++ -c function1.cpp

function2.o: function2.cpp
	g++ -c function2.cpp

#remove object files
clean:
	rm -rf *o hello
	
