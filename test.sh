if [ -z $1 ]
then
    echo "has not"
else
    echo "has $1"
fi

while getopts ":a:b:c:d:" opt  
do  
    case $opt in  
        a)  
        echo "参数 a 的值 $OPTARG"  
        ;;  
        b)  
        echo "参数 b 的值 $OPTARG"  
        ;;  
        c)  
        echo "参数 c 的值 $OPTARG"  
        ;;  
        d)
        echo "$OPTARG"
        ;;
        ?)  
        echo "未知参数"  
        exit 1;;  
    esac  
done 