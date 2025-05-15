## l33t-Benign (Part 2 of 133t-dangerous)

Part 2 description: Find out who was else was affected.

---

NAVI is eager to hack someone. And of course, the original name was NAVI in the script. CacheTheStamp3de also apparently can see all creds from all users, including konata's.

![alt text](images/image-52.png)

LOIC also provides a private key for the SAML login page, implying its vulnerable. This is how we can pretend to be another user.

![alt text](images/image-53.png)

As LOIC pointed out, Logging into the SimpleSAML page will show credentials if your username is linked to what was stolen. Since this account is new, it is empty.

However, if logged in, any account can see a list of credential UUIDs as a response.

![alt text](images/image-64.png)

Using Burp Suite and SAML Raider, the response to the POST on /saml/acs shows a username.

![alt text](images/image-62.png)

Somewhere in the network responses shows a /get_cred endpoint, although I forgot which one specifically.

![alt text](images/image-65.png)

By deleting the signature in this response entirely, and changing the username, we can 'become' other users and see credentials linked to their account with the /get_cred endpoint.

![alt text](images/image-66.png)

![alt text](images/image-67.png)

But for some reason they are not shown when it comes to CacheTheStamp3de, the user that supposedly has access to all credentials.

![alt text](images/image-63.png)

Looking closer at the public UUIDs, this one stands out as not on either LOIC or NAVIs accounts.

![alt text](images/image-68.png)

Trying to get this one directly will show message:

![alt text](images/image-70.png)

Who is Gr4deRaider? By retrying the SAML response as this user, the flag is revealed.

![alt text](images/image-71.png)
