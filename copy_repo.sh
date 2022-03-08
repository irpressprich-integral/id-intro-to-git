if ([[ -z $1 ]])
then
	echo "Please enter a git repo url"
else
	git branch -r | grep -v '\->' | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
	git pull --all
	git remote set-url origin $1
	git push --all
fi
