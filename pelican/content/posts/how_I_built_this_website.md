title: How I built this website
date: 2020-04-14
modified: 2020-04-25
slug: how-I-built-this-website
category: docs
summary: A bit of documentation to maintain a site with GitHub
cover: images/book.jpg

# How I built this website
---

I wanted to create my own website, so first I tried [Joomla](https://www.joomla.org/) next to my hosting provider [Strato](https://www.strato.com/). Not long before I had created an ecommerce store with [Wix](https://www.wix.com/) and a website with [Jimdo](www.jimdo.com), but this time I wanted full control.

After some hands-on time with Joomla and reading about [WordPress](https://wordpress.org/), I found CMS an overkill for the site in mind. So I turned to static website generators.

Since I code in Python and I am familiar with Markdown, I found [Pelican](https://blog.getpelican.com/) very appealing to my needs. I use [Anaconda](https://www.anaconda.com/) for my data science projects.

After I came across with [GitHub Pages](https://pages.github.com/), I decided to host the website from my own repository. Researching a bit, I found this step-by-step [guide](https://pythonforundergradengineers.com/how-i-built-this-site-1.html) very useful.

The repository of this website is available in [GitHub.](https://github.com/luisveratudela/luisveratudela.github.io)

## Maintenance

Website maintenance is as easy as with any other repository, since GitHub Pages publishes directly from its root. You can create a separate branch in GitHub to keep code and documentation separated, but I preferred to publish directly to the root.

I normally work from the Anaconda prompt. So first, you need to activate the environment created for the website and check that the local repository is up to date.

```text
(base) C:\activate staticsite
(staticsite) C:\cd repository
(staticsite) C:\repository> git pull origin master
```

 Pelican is in a subdirectory of the repository, since the website is published to its root. After website posts are created in Markdown, you need to publish them back to the root of the local repository. This step overwrites any previous content.  

```text
(staticsite) C:\repository\cd pelican
(staticsite) C:\repository\pelican>pelican -s pelicanconf.py -o .. content
```

More often than not I want to visualize the changes locally. So, I go to the output folder, which in this case is the root of the repository and open a local server using Python.

```text
(staticsite) C:\repository>python -m http.server
```

Once the website is correctly compiled, the next step is to push the local repository back to GitHub. GitHub Pages will take it from there and publish it.

```text
 (staticsite) C:\repository> git add .
 (staticsite) C:\repository> git commit -m "comment for documentation"
 (staticsite) C:\repository> git push origin master
```
