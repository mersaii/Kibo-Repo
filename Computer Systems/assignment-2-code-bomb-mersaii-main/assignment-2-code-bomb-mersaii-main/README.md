[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13415469)
# Assignment 2: Code Bomb

> This lab is from the textbook and supporting material [*Computer Systems: A Programmer's Perspective*](https://csapp.cs.cmu.edu/).

The nefarious *Dr. Evil* has planted a slew of "binary bombs" on our
class machines. A binary bomb is a program that consists of a sequence
of phases. Each phase expects you to type a particular string on
`stdin`. If you type the correct string, then the phase is *defused* and
the bomb proceeds to the next phase. Otherwise, the bomb *explodes* by
printing `"BOOM!!!"` and then terminating. The bomb is defused when
every phase has been defused.

There are too many bombs for us to deal with, so we are giving each
student a bomb to defuse. Your mission, which you have no choice but to
accept, is to defuse your bomb before the due date. Good luck, and
welcome to the bomb squad!

## Step 0: Prepare your Environment

As you will see below, you will be working with an executable that we generate
for you. This means, that the environment in which we build your code bomb
needs to be the same environment that you run and defuse your code bomb on.
Since students have all different types of machines, it would be impractical
to try to build the executables for everyone's individual configurations.
Therefore, for this assignment, you will need to work within a GitHub CodeSpace.  This
allows us to ensure that you will be using an x86-64 Linux environment, the same
type of environment on which we are running the bomb server.

1. Click this link and Accept the Assignment to clone your own copy of the
   repository: [Assignment2-Code-Bomb](https://classroom.github.com/a/hjD0u5HG).
2. Once the repository has been created, refresh the page and click the "Open
   in GitHub Codespaces" button.

You will now be within a Visual Studio code environment that is contained
within your web browser.  It has a terminal, and a full Linux environment.

You can return to the same Codespace at any time by visiting [https://github.com/codespaces](https://github.com/codespaces) and selecting the Codespace 
associated with this repository.  

## Step 1: Get Your Bomb

1. You can obtain your bomb by pointing your Web browser at:

       http://34.216.75.189:15213/

   This will display a binary bomb request form for you to fill in. Enter your
   GitHub alias and Kibo email address and hit the Submit button. The server
   will build your bomb and return it to your browser in a `tar` file called
   `bombk.tar`, where $k$ is the unique number of your bomb.

2. Once you have downloaded your bomb to your personal computer, you will need
   to upload it to your Codespace environment.  To do that, right-click within
   the "Explorer" pane of your environment and select "Upload".  Finally, select
   the `bombk.tar` file that you just downloaded to your computer and click
   "Open".  

3. Then, within the Codespace terminal, give the command: `tar -xvf bombk.tar`.
   This will create a directory called `./bombk` with the following files:

   - `README`: Identifies the bomb and its owners.
   - `bomb`: The executable binary bomb.
   - `bomb.c`: Source file with the bomb's main routine and a friendly
      greeting from Dr. Evil.

4. At this point, it is probably a good idea to go ahead and commit the
   downloaded bomb and the untarred files to your repo so that if your Codespace
   is ever lost, you still have the same bomb that you have been working on in
   a safe place.

If for some reason you request multiple bombs, this is not a problem.
Choose one bomb to work on and delete the rest.

## Step 2: Defuse Your Bomb

Your job for this assignment is to defuse your bomb.

You must do the assignment in GitHub Codespaces. In fact, there
is a rumor that Dr. Evil really is evil, and the bomb will always blow
up if run elsewhere. There are several other tamper-proofing devices
built into the bomb as well, or so we hear.

You can use many tools to help you defuse your bomb. Please look at the
**hints** section for some tips and ideas. The best way is to use your
favorite debugger to step through the disassembled binary.

Each time your bomb explodes it notifies the bomblab server, and you
lose 1/2 point (up to a max of 20 points) in the final score for the
lab. So there are consequences to exploding the bomb. You must be
careful!

The first four phases are worth 10 points each. Phases 5 and 6 are a
little more difficult, so they are worth 15 points each. So the maximum
score you can get is 70 points.

Although phases get progressively harder to defuse, the expertise you
gain as you move from phase to phase should offset this difficulty.
However, the last phase will challenge even the best students, so please
don't wait until the last minute to start.

The bomb ignores blank input lines. If you run your bomb with a command
line argument, for example,

```bash
linux> ./bomb psol.txt
```

then it will read the input lines from `psol.txt` until it reaches EOF
(end of file), and then switch over to `stdin`. In a moment of weakness,
Dr. Evil added this feature so you don't have to keep retyping the
solutions to phases you have already defused.

To avoid accidentally detonating the bomb, you will need to learn how to
single-step through the assembly code and how to set breakpoints. You
will also need to learn how to inspect both the registers and the memory
states. One of the nice side-effects of doing the lab is that you will
get very good at using a debugger. This is a crucial skill that will pay
big dividends for the rest of your career.

## Scoreboard

The bomb will notify your instructor
automatically about your progress as you work on it. You can keep track
of how you are doing by looking at the class scoreboard at:

    http://34.216.75.189:15213/scoreboard

This web page is updated continuously to show the progress of each
bomb.

## Hints *(Please read this!)*

There are many ways of defusing your bomb. You can examine the assembly in great
detail without ever running the program, and figure out exactly what it does.
This is a useful technique, but it is not always easy to do. You can also run it
under a debugger, watch what it does step by step, and use this information to
defuse it. This is probably the fastest way of defusing it.

We do make one request, *please do not use brute force!* You could write
a program that will try every possible key to find the right one. But
this is no good for several reasons:

- You lose 1/2 point (up to a max of 20 points) every time you guess incorrectly
  and the bomb explodes.
- Every time you guess wrong, a message is sent to the bomblab server. You could
  very quickly saturate the network with these messages, and cause the system
  administrators to revoke your computer access.
- We haven't told you how long the strings are, nor have we told you what
  characters are in them. Even if you made the (incorrect) assumption that
  they all are less than 80 characters long and only contain letters, then you
  will have $26^{80}$ guesses for each phase. This will take a very long time
  to run, and you will not get the answer before the assignment is due.

Many tools are designed to help you figure out both how
programs work, and what is wrong when they don't work. Here is a list of
some of the tools you may find useful in analyzing your bomb, and hints
on how to use them.

- `gdb`
  The GNU debugger is a command-line debugger tool available on
  virtually every platform. You can trace through a program line by
  line, examine memory and registers, look at both the source code and
  assembly code (we are not giving you the source code for most of
  your bomb), set breakpoints, set memory watch points, and write
  scripts.

  The CS:APP website:

    http://csapp.cs.cmu.edu/public/students.html

  has a very handy single-page `gdb` summary that you can print out
  and use as a reference. Here are some other tips for using `gdb`.

  - To keep the bomb from blowing up every time you type in a wrong
    input, you'll want to learn how to set breakpoints.

  - For online documentation, type "`help`" at the `gdb` command
    prompt, or type "`man gdb`", or "`info gdb`" at a Unix prompt.
    Some people also like to run `gdb` under `gdb-mode` in `emacs`.

- `objdump -t`

  This will print out the bomb's symbol table. The symbol table
  includes the names of all functions and global variables in the
  bomb, the names of all the functions the bomb calls, and their
  addresses. You may learn something by looking at the function names!

- `objdump -d`

  Use this to disassemble all of the code in the bomb. You can also
  just look at individual functions. Reading the assembler code can
  tell you how the bomb works.

  Although `objdump -d` gives you a lot of information, it doesn't
  tell you the whole story. Calls to system-level functions are
  displayed in a cryptic form. For example, a call to `sscanf` might
  appear as:

        8048c36:  e8 99 fc ff ff  call   80488d4 <_init+0x1a0> 

  To determine that the call was to `sscanf`, you would need to
  disassemble within `gdb`.

- `strings`

  This utility will display the printable strings in your bomb.

Looking for a particular tool? How about documentation? Don't forget,
the commands `apropos` and `man` are your friends. In
particular, `man ascii` might come in useful. `Also, the web
may also be a treasure trove of information. If you get stumped, please
post your submission to the course Discord page.

## Grading

As described above, the points that you earn for this assignment will be
based on how many times you explode the bomb (1/2 point penalty each time) and
the number of stages that you successfully defuse.  You earn 10 points per
stage for the first 4 stages, and 15 points per stage for the final two stages
(since they are a bit more difficult), for a maximum possible score of 70 points.

## Submitting Your Work

Your work must be submitted to Anchor for degree credit and to Gradescope for
grading.

1. After you have obtained your bomb, untar it using the instructions above, and
   then commit the newly generated directory to your repo. As you defuse a
   particular stage of the bomb, add the string to the `solution.txt`` file.
2. Ensure that you `commit` and `push` your local code changes to your remote
   repository.
3. Upload your submission to [Gradescope](https://www.gradescope.com) via the
   appropriate submission link by selecting the correct GitHub repository from
   the drop-down list.
4. Export a zip archive of your GitHub repository by visiting your repo on
   [GitHub](https://www.github.com), clicking on the green `Code` button, and
   selecting "Download Zip".
5. Upload the zip file of your repository to Anchor using the form below.
