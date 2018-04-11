#include <gtest/gtest.h>
#include <gmock/gmock.h>


struct Mock
{
    MOCK_METHOD1(method, void(int));
};

TEST(testGMockMain, testGMockMain)
{
    const int value = 42;
    
    Mock mock;
    EXPECT_CALL(mock, method(value))
        .Times(1);
        
    mock.method(value);
}
