# NorMatrix
check some norm for you

## checks :

- [x] 80 cols per line
- [x] space/tab alone (in a line)/(at the end of line)
- [x] two newline at end of file
- [x] two newline between function (between all buf chhhtt)
- [x] libc function call (pr welcome to add some libc function always banned)
- [x] nested branch more than 3 branch
- [x] no more than 20 lines per function
- [x] comma with no space after
- [x] end of parenthesis with a open curly bracket next `){`
- [x] star char `*` like this `char* buf`
- [x] preprocessors indentations (`#if..`, `#endif`)
- [x] multiple statements
- [ ] ...

## example if you run it as a github workflow
this is not the latest normatrix but :
[link](https://github.com/Saverio976/NorMatrix/runs/4702369332?check_suite_focus=true)
(this workflow pass well, but it will not if you copy the code below)

## doc
#### Makefile
```
USAGE:
	make [-C path/to/NorMatrix] [rule] [VAR=VALUE]
DESCRIPTION:
	check the norm!
ARGS:
	-C path/to/NorMatrix		if you are on another working directory
					than NorMatrix, add this.

	rule				the rule to execute ('all', 'update',
					'up', 'tests_run'). If you dont say
					any rule, it will do the 'all' rule.

	VAR=VALUE			to set a different value for a
					specific var. Allow to change the
					directory to check.
					you will probably do:
					make -C path/NorMatrix PATH_CHECK=$PWD
```
#### exec.sh
```
USAGE:
	./exec.sh
DESCRIPTION:
	call the makefile for the all rule with PATH_CHECK to your current
	working directory
ARGS:
	NO
```

## run it as a github workflow
in the repo root :
```bash
mkdir .github
mkdir .github/workflows
echo '
name: NorMatrix Check

on: [push]

jobs:
  norm:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: clone NorMatrix
      run: git clone https://github.com/Saverio976/NorMatrix

    - name: NorMatrix
      run: make -C NorMatrix/ PATH_CHECK=$PWD
' > .github/workflows/normatrix_check.yml
```

## run it with an alias
with this, you will can just write `normatrix` in a shell and it will check
the norm for your current working directory

if you are using bash shell:
```bash
echo alias normatrix="$PWD/exec.sh" >> $HOME/.bashrc
```
if you are using zsh shell:
```bash
echo alias normatrix="$PWD/exec.sh" >> $HOME/.zshrc
```
else, handle thsi yourself bruh

## Contribute
if you want to add some checkers (in python, bash, or node),
add a file in src/ folder with a filename clear enouth.

if the filename is `test.sh`, the file wiil be executed like this `./src/test.sh {file to check}`

If there is one error or more, exit with the number of error, else 
status code 0. You must print the filename and the line where the error is

[more preicse information on the file : CONTRIBUTING.md]

### thanks

chempa for his sample of file that dont follow the epitech norm
