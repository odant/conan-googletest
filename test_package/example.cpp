#include <gtest/gtest.h>
#include <gmock/gmock.h>

TEST(Example, simple)
{
    ASSERT_TRUE(true);
}

struct Mock
{
    MOCK_METHOD1(method, void(int));
};

TEST(Example, mocking)
{
    const int value = 42;
    
    Mock mock;
    EXPECT_CALL(mock, method(value))
        .Times(1);
        
    mock.method(value);
}