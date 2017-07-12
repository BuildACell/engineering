---
layout: page
title: Contribute
categories: metaproject
mainmenu: true
weight: 10
published: true
---

Build-A-Cell is a distributed and global project. If you're captivated by any aspect of the project, get going and share your work. Yearning to build a cell but don't know where to begin? Follow the instructions on this page and start contributing.

## Contributing to the Website
There are a number of ways to contribute to this website. Regardless of which option you choose, you'll need to make an account on [GitHub](https://github.com/join). Your account then needs to be added to the Build-A-Cell team. Please [contact us](mailto:atg@buildacell.io) to get added to the team, or check the 'Forking the Repository' section of this document for other options.

Once you have a GitHub account, there are three options for editing the website: prose.io, which is easier but less powerful; directly editing in github, and downloading a local copy of the repository.

### Editing in GitHub

Once you have access to the GitHub repository, open the repository at [https://github.com/BuildACell/engineering](https://github.com/BuildACell/engineering), navigate to the file you want to edit, open it and click the 'edit' pen icon in the top right of the viewer pane. An editor will open, although it does not have helper functions for Markdown. You can preview using the 'Preview changes' button at the top. Once satisfied, fill out a commit message and commit your changes using the button at the bottom of the page.

### Editing Locally

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

### Forking the Repository

If you don't have access to the main Build-A-Cell repositories, you can instead [fork](https://help.github.com/articles/fork-a-repo/) them. This creates your own copy of the repository on GitHub. You can then make changes to this version, following the above instructions, and submit a [pull request](https://help.github.com/articles/about-pull-requests/) to have the change integrated into the main website. See the [GitHub documentation](https://help.github.com/) for more details.

### Other Resources

Our data sharing relies on Git for eash of collaborating on code, information and documentation. Check out the following resources to learn more about the component technologies:

* [Git Book](https://git-scm.com/book/en/v2)
* [GitHub documentation](https://help.github.com/)
* [Jekyll documentation](https://jekyllrb.com/docs/home/)
* [Jekyll on GitHub Pages](https://pages.github.com)
