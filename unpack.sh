#!/bin/bash

# read file type
type=$(file $1)
# check types
echo $type

case $type in
  *"ZPAQ"* )
    mv $1 $1.zpaq
    zpaq x $1.zpaq
  ;;
  *"XZ"* )
    mv $1 $1.xz
    xz -d $1.xz
  ;;
  *"bzip2"* )
    mv $1 $1.bz
    bunzip2 $1.bz
  ;;
  *"LZMA"* )
    mv $1 $1.lzma
    unlzma $1.lzma
  ;;
  *"POSIX tar"* )
    mv $1 $1.tar
    tar --posix -xvf $1.tar
  ;;
  *"lzip"* )
    mv $1 $1.lz
    lzip -d $1.lz
  ;;
  *"7-zip"* )
    mv $1 $1.7z
    7z x $1.7z
  ;;
  *"ARJ"* )
    mv $1 $1.arj
    arj x $1.arj
  ;;
  *"RAR"8 )
    mv $1 $1.rar
    rar e $1.rar
  ;;
  *"gzip"* )
    mv $1 $1.gz
    gunzip $1.gz
  ;;
  *"Zoo"* )
    mv $1 $1.zoo
    zoo -extract $1.zoo
  ;;
  *"Zip"* )
    mv $1 $1.zip
    unzip $1.zip
  ;;
  *"NuFile"* )
    mv $1 $1.nu
    dd if=./$1.nu of=./$1 bs=1 skip=388
  ;;
    
esac
