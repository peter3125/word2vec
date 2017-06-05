#!/bin/bash

DATA_DIR=../data
BIN_DIR=../bin
SRC_DIR=../src

TEXT_DATA=$DATA_DIR/wn2vec.txt
VECTOR_DATA=$DATA_DIR/wordnet_semantic_vecs.bin

pushd ${SRC_DIR} && make; popd

if [ ! -e $VECTOR_DATA ]; then
  echo -----------------------------------------------------------------------------------------------------
  echo -- Training vectors...
  time $BIN_DIR/word2vec -train $TEXT_DATA -output $VECTOR_DATA -cbow 0 -size 3 -window 2 -negative 0 -hs 1 -sample 1e-3 -threads 20 -binary 0

fi

echo -----------------------------------------------------------------------------------------------------
echo -- distance...

$BIN_DIR/distance $DATA_DIR/$VECTOR_DATA
