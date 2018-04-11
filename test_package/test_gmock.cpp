#include <gtest/gtest.h>
#include <gmock/gmock.h>


struct Mock
{
    MOCK_METHOD1(method, void(int));
};

TEST(testGMock, testGMock)
{
    const int value = 42;
    
    Mock mock;
    EXPECT_CALL(mock, method(value))
        .Times(1);
        
    mock.method(value);
}


int main(int argc, char** argv) {

    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
