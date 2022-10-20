"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands
where each command will be of the  types listed above. Iterate through each
command in order and perform the corresponding operation on your list.

Example
N =  4
append 1
append 2
insert 3 1
print

"""

if __name__ == '__main__':
    N = int(input())
    l = []
    while N >=0:
        cmd = input()
        cmd = cmd.split(" ")
        lcmd = cmd[0] #list command
        if len(cmd) == 1:
            # print command
            if lcmd == 'print':
                print(l)
        elif len(cmd) == 3:
            # insert command
            pass
        else:
            # other commands
            vcmd = cmd[1] #value command
            call = getattr(l, vcmd)
            call

        N = N - 1
