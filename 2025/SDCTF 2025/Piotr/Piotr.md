# OSINT

## Piotr

In this sequence of challenges, we have to find out where Piotr (a fake person) was on certain days. All we know in the beginning is that he is associated with San Diego's **ACM** branch.

### Initial Recon

Going to the **ACM** website and looking through the officers we find the man, his last name and his **LinkedIn** page.

![alt text](./images/image-1.png)

Screenshot credit: Lizazal on GitHub.

https://www.linkedin.com/in/piotr-sultanbekov/

The Bio contains a link to Piotr's **GitHub** website

![alt text](./images/image-2.png)

The education section shows Piotr has an interest in **Smash Club**, which is referencing the video game series _Super Smash Bros_, available on various Nintendo consoles.

![alt text](./images/image-3.png)

The GitHub website has a link to the actual GitHub account in the footer: **sultangamer06**

![alt text](./images/image-4.png)

The about page tells us that Piotr's favorite character to play as in _Smash Bros_ is **Isabelle**.

![alt text](./images/image-5.png)

Piotr's GiHub profile is sparse except for one repository with 13 commits.

![alt text](./images/image-6.png)

Commit e8e80a6 hints that Piotr has an account on X, formerly known as Twitter.

![alt text](./images/image-7.png)

There are also 11 deployments of this repository.

![alt text](./images/image-8.png)

One of these is a failed deployment, which shows the X-formerly-known-as-twitter handle: **sultangam3r**

![alt text](./images/image-9.png)

Following this trail, we find the account has **Isabelle** in the banner, and a **Truth Social** profile: **sultangamer**

![alt text](./images/image-10.png)

Piotr's **Truth Social**

![alt text](./images/image-15.png)

## Day 4: What city did Piotr go to May 7th?

One post on Truth Social has an image of a gas station. Piotr says it's in Texas, but it doesn't look like Texas. There are lots of different languages on the signage, one of which says **STB Bank**

![alt text](./images/image-16.png)

![alt text](./images/image-19.png)

**STB Bank** is a state bank headquartered in **Tunis**, Tunisia.

![alt text](./images/image-17.png)

Here is the logo of the bank. It looks similar to the photo.

![alt text](./images/image-18.png)

**Tunis** is the flag.

## Day 5: What city did Piotr go to on May 8th?

The latest post on Truth Social has Piotr saying he's going to where the "sky is bluer". This is a hint to the website **Bluesky**.

![alt text](./images/image-20.png)

Using `whatsmyname.app` on `sultangamer` gives a positive result for **Bluesky**

![alt text](./images/image-21.png)

Piotr's last name matches the account.

![alt text](./images/image-22.png)

This account is also following UC San Diego.

![alt text](./images/image-23.png)

Posts from May 8th imply that Piotr may have been as a **Super Smash Bros Tournament**, but couldn't stay for the main event. The first part of the this is written in **German**.

![alt text](./images/image-24.png)

Back on the X-formerly-known-as-twitter account, Piotr is following a **German** **Smash Melee Tournament** account.

![alt text](./images/image-13.png)

Googling for these details gives a result of a tournament in **Großlohra**.

![alt text](./images/image-25.png)

The flag is **Großlohra**.

## Day 6: What city did Piotr go to on May 9th?

On Bluesky, Piotr mentioned needing to "go somewhere important tomorrow" on May 8th.

![alt text](./images/image-26.png)

Then on May 9th, this post.

![alt text](./images/image-27.png)

The language is **Kazakh**, the language of **Kazakhstan**.

![alt text](./images/image-28.png)

Using bing for "Piotr Sultanbekov" gives this result of vk.com, which has **ditto.ai**

![alt text](./images/image-29.png)

**ditto** is another account that Piotr follows on X-formerly-known-as-twitter.

![alt text](./images/image-30.png)

This bio contains UCSD, and when the russian is translated, confirms that this is our Piotr, because it's the same bio as on Truth Social.

![alt text](./images/image-31.png)

![alt text](./images/image-32.png)

The latest post on VK is blurred, but is dated for May 9th.

![alt text](./images/image-33.png)

The map location at the top of the post can be translated to **Baikonur**.

![alt text](./images/image-34.png)

Baikonur contains the Baikonur Cosmodrome in Kazakhstan, which is a space launch facility. The image is a blurred image of an astronaut.

![alt text](./images/image-35.png)

The flag is **Baikonur**.

## Day 3: What city did Piotr go to on May 6th?

Using `sultangamer06`, the username from GitHub, and searching with `osint.rocks`, a number of results are returned. Most of these are false positives.

Imgur however, is related.

![alt text](./images/image-37.png)

Even though the account is empty originally.

![alt text](./images/image-38.png)

If we google search `imgur sultangamer06`, 3 results comes back. that are related.

![alt text](./images/image-36.png)

The third is dated for May 9th. He went to a **magdalena bay** concert on Tuesday, which is May 6th.

![alt text](./images/image-39.png)

Searching for past concerts by this artist on songkick.com shows the city Piotr was in.

![alt text](./images/image-40.png)

The flag is **Buffalo**

## Day 2: What city did Piotr go to on May 5th?

Backtracking, the ACM UCSD Instagram followers list appears to have Piotr.

![alt text](./images/image-41.png)

The first post is Piotr at a beach on May 5th. Which beach?

![alt text](./images/image-44.png)

Using a Google reverse image search, this pier is located at Kitty Hawk, North Carolina.

![alt text](./images/image-42.png)

The flag is **Kitty Hawk**.

## Day 1: What city did Piotr visit on May 4th?

On X-formerly-known-as-twitter, Piotr made a post on May 4th saying they were leaving San Diego to find love. Where did he go?

![alt text](./images/image-11.png)

Looking at who Piotr's following shows one account **Plumeria**

![alt text](./images/image-12.png)

**Plumeria** is a dating app, according to their website at https://goplumeria.com/

![alt text](./images/image-14.png)

Another post on the Instagram has a hashtag that could be unique to Piotr.

![alt text](./images/image-43.png)

A google search for this hashtag returns a Reddit result.

![alt text](./images/image-45.png)

One of the commenters has a variant of the sultan gamer username and uses this hashtag.

![alt text](./images/image-46.png)

One of the posts by this user has a QR code for a party on May 2nd. Not the date we need, but could be related.

![alt text](./images/image-47.png)

Scanning this QR code links to a **Plumeria** schedule on May 4th, for the "most pedestrian-friendly city in America". Which city is this?

![alt text](./images/image-48.png)

Looking up **Buffalo Bayou Park Cistern** and **Rice University** will lead to Houston, Texas.

The flag is **Houston**.
