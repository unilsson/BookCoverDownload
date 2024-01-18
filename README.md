# push-to-git
A simple script that semi-automizes the push of stuff to github. The github token is kept in a separate file `/home/<user>/.git_token`, which contains
`GIT_TOKEN=<token string>` and `GIT_USERNAME=<github user name>`

The script is called as `push-to-git <commit text>`

The script should be put in the git repository directory. If you want you can skip synzhing the actual script to github.com by fixing the .gitignore file. It is OK to synch the script since it contains no secret information.

