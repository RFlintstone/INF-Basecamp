read -p "The script will do a hard reset and pull the latest files. Are you sure? (y/n)?" choice
case "$choice" in
  y|Y )
  git reset --hard
  git pull
  ;;
  n|N )
  echo "Canceling operation"
  ;;
  * )
  echo "Invalid choice. Please run the script again."
  ;;
esac