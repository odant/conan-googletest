#include <gtest/gtest.h>
#include <filesystem>


#ifdef _MSC_VER
using namespace std::experimental::filesystem;
#else
using namespace std::filesystem;
#endif


TEST(testGTestMain, testGTestMain) {
    const path path1 = "/home/user/folder";
    std::cout << ::testing::PrintToString(path1) << std::endl;
}
