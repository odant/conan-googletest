#include <gtest/gtest.h>
#include <filesystem>


#if defined(HAVE_CXX_STD_FILESYSTEM)
namespace fs = std::filesystem;
#elif defined(HAVE_CXX_EXPERIMANTAL_FILESYSTEM)
namespace fs = std::experimental::filesystem;
#else
#error "Can`t detect filesystem namespace"
#endif


TEST(testGTestMain, testGTestMain) {
    const fs::path path1 = "/home/user/folder";
    std::cout << ::testing::PrintToString(path1) << std::endl;
}
