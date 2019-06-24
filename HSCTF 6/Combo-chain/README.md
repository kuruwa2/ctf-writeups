## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Combo Chain</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Pwn</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>combo-chain   combo-chain.c</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

#### Message
Written by: Ptomerty

I've been really into Super Smash Brothers Melee lately...

nc pwn.hsctf.com 2345

Note: If you're trying to use python or a similar program to run your exploit, make sure to keep stdin alive with cat, like this: (python; cat -) | nc pwn.hsctf.com <port>

libc SHA-1: 238e834fc5baa8094f5db0cde465385917be4c6a libc.so.6 libc6_2.23-0ubuntu11_amd64

6/3/19 7:35 AM: Binary updated, SHA-1: 0bf0640256566d2505113f485949ec96f1cd0bb9 combo-chain

## Note
This writeup is constucted after author seeing the [neat code written by Defenit](https://ctftime.org/writeup/15660), being a small note on learning using ond-gadget and elf after the CTF.

## Solution
