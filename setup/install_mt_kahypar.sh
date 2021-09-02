# Install MtKaHyPar

cd partitioner/mt-kahypar
git submodule init
git submodule update

rm -rf build
mkdir build
cd build
/home/tobias/cmake-3.18.1-Linux-x86_64/bin/cmake .. -DCMAKE_BUILD_TYPE=RELEASE
make MtKaHyParFast -j8
make MtKaHyParStrong -j8
cd ../../..