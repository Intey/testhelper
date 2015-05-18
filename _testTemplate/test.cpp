#include <gtest/gtest.h>
#include <testhelpers/core.h>
#include <testhelpers/paths.h>

/*! Класс для функций, выполняемых перед кейсом тестов или каждым тестом.*/
class TestCaseName : public ::testing::Test {
protected:
    /*! Выполняется перед кейсом.*/
    static void SetUpTestCase()
    {
        //shared_resource_ = new ...; // создаем общий ресурс
        Helps::createLogger();
    }

    /*! Выполняется после кейса.*/
    static void TearDownTestCase()
    {
        //delete shared_resource_;
        //shared_resource_ = NULL;
    }

    /*! Выполняется перед каждым тестом.*/
    virtual void SetUp() {}
    /*! Выполняется после каждого теста.*/
	virtual void TearDown() {}

    // Some expensive resource shared by all tests.
    //static T* shared_resource_; ///< общий ресурс для тестов кейса
};

//T* FooTest::shared_resource_ = NULL;  //инициализируем ресурс

TEST_F(TestCaseName, RigthCase) {
  FAIL() << "Write expecting behaviour test";
}

TEST_F(TestCaseName, WrongCase) {
  FAIL() << "Write test for 'wrong data' case";
}



