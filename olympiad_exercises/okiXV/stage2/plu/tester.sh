for i in {1..10} ; do
  echo test "${i}":
  python3 test_generator.py > input.in
  time python3 cze.py < input.in > output.out
  echo brut time:
  time python3 brut.py < input.in > brut_output.out
  diff -bew output.out brut_output.out || { echo Fail ; break; }
  echo Success
done
