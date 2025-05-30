# Sending Mixed Signals

![alt text](images/image.png)

The website has this form:

![alt text](images/image-1.png)

Looking up the name of the mock-version: TM Signal

![alt text](images/image-2.png)

Looking up the source code.

![alt text](images/image-3.png)

The relevant hard-coded credential is shown in the article:

https://micahflee.com/heres-the-source-code-for-the-unofficial-signal-app-used-by-trump-officials/

![alt text](images/image-4.png)

The article doesn't show the the author or commit information, so I found the repository online.

![alt text](images/image-6.png)

On GitHub you can find the email associated with a commit by cloning the repo and looking at the git log on this commit. However, Davidt's email turned out to be incorrect? Why? Because Davidt's commit is just moving things to a new folder during this 7.2.4.2 Release This implies the credential existed before this release somewhere else.

![alt text](images/image-5.png)

This command just adds all of the release names into a file

![alt text](images/image-7.png)

Below is a PowerShell script that looks through all of the releases for this credential and finds the first instance of it and the file.

![alt text](images/image-8.png)

After running, the result was `Release_5.4.11.20`, and the file in question was just in `main` instead of `tm` like the originally seen commit from `Davidt`.

This release name is the answer for part 3.

![alt text](images/image-9.png)

Running `blame` on this file shows it was `moti` and not `Davidt` that actually added hard-coded this credential.

![alt text](images/image-10.png)

Running `show` for the commit on this line gives back the email needed for part 2:

![alt text](images/image-11.png)

The flag was: flag{96143e18131e48f4c937719992b742d7}.

![alt text](images/image-12.png)
