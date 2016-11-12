---
layout: page
title: Contribute
categories: metaproject
mainmenu: true
weight: 10
published: true
---

Build-A-Cell is a distributed and global project. If you're captivated by any aspect of the project, get going and share your work. Yearning to build a cell but don't know where to begin? Check our [list of ideas](/engineering/about/bootsequence/) for a place to start.

# Contributing to the Website
There are a number of ways to contribute to this website. Regardless of which option you choose, you'll need to make an account on [GitHub](https://github.com/join). Your account then needs to be added to the Build-A-Cell team. Please [contact us](mailto:atg@buildacell.io) to get added to the team, or check the 'Forking the Repository' section of this document for other options.

Once you have a GitHub account, there are two options for editing the website: prose.io, which is easier but less powerful, and downloading a local copy of the repository.

## Editing with prose.io
[Prose.io](http://prose.io) is an easy-to-use online editor with support for both Markdown (the format we write web pages in), and GitHub pages/Jekyll (the technology that generates our website). To use prose.io, just [visit the website](http://prose.io) and authenticate with your GitHub account. You will then see a list of the repositories to which you have access. Filter by BuildACell in the right panel, and select the 'engineering' project from the list.

You will be presented with a list of files and directories available for editing. There are two kinds of webpages you can add: *pages*, which form the main website, and *posts*, which are dated and presented as updates or entries in a lab notebook. To edit a page or post, navigate to it and open it in prose. To create a new page, choose the appropriate directory (about, devkit, etc), and create a new file within it. To create a new post, create a file under the `_posts` directory and ensure its filename begins with the date. All file names should be lowercase, separated by hyphens, and end in `.md` for markdown. 

For example, to create a new page relating to the development kit, navigate to the `devkit` directory and create a new file. Prose will suggest a filename at the top, change this to reflect the page: `my-new-page.md`. Note that we do not include the date, since this is a page.

You can now create the pages content by directly entering [Markdown](http://daringfireball.net/projects/markdown/) or using the widgets to insert headers, links, etc. To link to other pages on the website, the easiest means is to make a markdown link pointing to the page's *relative path*. On our website, this looks like `/engineering/<directory>/<page name>/`. For example, to link to the 'Unix philosophy' page in the 'about' section, we would link to `/engineering/about/unix-philosophy/`. The overall markdown code looks like: `[Unix Philosophy](/engineering/about/unix-philosophy/)`.

Once you have finished creating or editing the new page, you can preview it by clicking on the eye icon to the right of the editor. If the page is correct, the next step is to *commit* it to the git repository. This adds your changes to the permanent history of the website, and publishes it online. For more information, see our instructions on [git](#git) below.

To commit, click on the save icon to the right. You will be presented with a list of your changes and a commit button. Add a message describing your changes (for example, "Added new instructions on how to contribute"), and click commit. Your changes should be visible on the website shortly.

Prose has more features, such as writing draft posts (which won't be visible on the website) and then publishing them later. Check out the internal help for more details.

## Editing Locally

Downloading the website repository locally is more complex than using Prose, but has several advantages: you can make more changes, saving intermediate results, without affecting the main website; it is easier to move files around; it is easier to add additional files such as experimental data and analysis; and all of the collaborative power of git can be used to work on both analysis and documentation.

The first step in working locally is to [clone the repository](https://github.com/BuildACell/engineering). If you don't know how to set up git and clone something locally, we would recommend following through the [Github Bootcamp](https://help.github.com/articles/set-up-git/) documentation, and perhaps have a look at the [Git Book](https://git-scm.com/book/en/v2). You can clone the repository by opening a terminal, navigating to the directory you want to store Build-A-Cell work in, and running: `git clone git@github.com:BuildACell/engineering.git`. You only need to clone the repository once, but before making new changes it will be useful to run `git pull`, to pull down the new changes to the website since you last updated.

The full Build-A-Cell engineering repository is now on your local machine, including its history. You can edit files using the editor of your choice: [Sublime](https://www.sublimetext.com) works well for editing both Markdown and code on OS X. Other Markdown editors also exist, some with preview capacity.

To get a local preview of the entire site, you'll need to build a copy of it on your own machine. The website is built using a tool called [Jekyll](https://jekyllrb.com/), which converts the Markdown files and other information in git into HTML, with an appropriate file structure. When you commit changes into git and push them to the main repository on GitHub, this tool is run for you, building the site and making the new version live at [http://buildacell.io/engineering](http://buildacell.io/engineering/). To run it locally, you need to install Ruby and download the Jekyll RubyGem. If you're on a Mac, you have a local copy of Ruby already. Otherwise, download it from [http://ruby-lang.org/](https://www.ruby-lang.org/en/downloads/). Next, enter the terminal, naviate to your Build-A-Cell engineering repository directory (where you cloned the repository above), and run the command `bundle install`.

This installs Jekyll and its requirements. You can now run `bundle exec jekyll serve`. This will start a webserver on your local machine, where you can browse a copy of the website as it will look after your edits. By default, the website will be available at [http://localhost:4000/engineering](http://localhost:4000/engineering); be sure to add the /engineering to the URL if you navigate by hand. As you edit files, this website will update to match the changes.

Make edits to files as described above in the section on Prose. Once you're finished, you need to stage and commit your changes. While the specific of using git are out of scope of this document (check the [Git Book](https://git-scm.com/book/en/v2) for more details), you can commit all of your changes by running the following terminal commands in the engineering directory:

```
git add .
git commit
```

You will be prompted to add a commit message describing your changes, which will then be committed as a version in your local repository. You can now push these changes up to the live site by running `git push`.

## Forking the Repository

If you don't have access to the main Build-A-Cell repositories, you can instead [fork](https://help.github.com/articles/fork-a-repo/) them. This creates your own copy of the repository on GitHub. You can then make changes to this version, following the above instructions, and submit a [pull request](https://help.github.com/articles/about-pull-requests/) to have the change integrated into the main website. See the [GitHub documentation](https://help.github.com/) for more details.

## Other Resources

Our data sharing relies on Git for eash of collaborating on code, information and documentation. Check out the following resources to learn more about the component technologies:

* [Git Book](https://git-scm.com/book/en/v2)
* [GitHub documentation](https://help.github.com/)
* [Jekyll documentation](https://jekyllrb.com/docs/home/)
* [Jekyll on GitHub Pages](https://pages.github.com)
