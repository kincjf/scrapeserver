#!/bin/sh

while getopts ":a:p:" opt; do
  case $opt in
    a) arg_1="$OPTARG"
    ;;
    p) p_out="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    exit 1
    ;;
  esac

  case $OPTARG in
    -*) echo "Option $opt needs a valid argument"
    exit 1
    ;;
  esac
done

printf "Argument p_out is %s\n" "$p_out"
printf "Argument arg_1 is %s\n" "$arg_1"

# imageName=xx:my-image
# containerName=my-container

# docker build -t $imageName -f Dockerfile  .
# docker build -t $imageName -f Dockerfile  .


# changed_files="$(git diff-tree -r --name-only --no-commit-id ORIG_HEAD HEAD)"
# changed_files="$(git diff-tree -r --name-only --no-commit-id FETCH_HEAD HEAD)"

# check_run() {
#     echo "$changed_files" | grep --quiet "$1" && eval "$2"
# }

# check_run package.json "npm install"

# echo 123123123
# npm install

# CMD="docker run -e SMF_CONFIG=$SMF_CONFIG ${NAME}${TAG} $@"

# echo ">> $CMD"
# $CMD

# 
# docker run --name=asdf -v /docker/data/...:/data

