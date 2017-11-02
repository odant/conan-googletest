SET PACKAGE=googletest/1.8.0
SET CHANNEL=odant/stable

SET COMPILER="Visual Studio"
SET COMPILER_VERSION=15
SET COMPILER_TOOLSET=v140_xp

conan create %PACKAGE%@%CHANNEL% ^
-s arch=x86 -s build_type=Release -s compiler=%COMPILER% -s compiler.runtime=MD -s compiler.version=%COMPILER_VERSION% -s compiler.toolset=%COMPILER_TOOLSET% -s os=Windows
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

conan create %PACKAGE%@%CHANNEL% ^
-s arch=x86 -s build_type=Debug -s compiler=%COMPILER% -s compiler.runtime=MDd -s compiler.version=%COMPILER_VERSION% -s compiler.toolset=%COMPILER_TOOLSET% -s os=Windows
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

conan create %PACKAGE%@%CHANNEL% ^
-s arch=x86_64 -s build_type=Release -s compiler=%COMPILER% -s compiler.runtime=MD -s compiler.version=%COMPILER_VERSION% -s compiler.toolset=%COMPILER_TOOLSET% -s os=Windows
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%

conan create %PACKAGE%@%CHANNEL% ^
-s arch=x86_64 -s build_type=Debug -s compiler=%COMPILER% -s compiler.runtime=MDd -s compiler.version=%COMPILER_VERSION% -s compiler.toolset=%COMPILER_TOOLSET% -s os=Windows
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%
