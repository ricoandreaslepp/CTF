# CTF write ups
Just a webpage for various CTF challenges I've solved.

# picoCTF

# CTFLearn

## Wikipedia
<code>Not much to go off here, but it’s all you need: Wikipedia and 128.125.52.138.</code>

In Wikipedia you can search for edits that were made but not accepted. So all you got to do in this challenge is go to https://wikipedia.com and paste the <code>128.125.52.138</code>.

A warning box pops up that says _This is an old revision of this page, as edited by 128.125.52.138 (talk) at 17:13, 17 August 2015 (add another type of flag). The present address (URL) is a permanent link to this revision, which may differ significantly from the current revision._ So after that it's easy enough to just CTRL+F and type in <code>CTF</code> after that we see that here was a previous section called _Competitions_ and there's the flag:

<code>In a certain CTF competition, the flag to a certain problem is "cNi76bV2IVERlh97hP".</code>
