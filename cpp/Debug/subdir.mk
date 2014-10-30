################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../common.cpp \
../problem001.cpp \
../problem002.cpp \
../problem003.cpp \
../problem004.cpp \
../problem005.cpp \
../problem006.cpp \
../problem007.cpp \
../problem008.cpp \
../problem009.cpp \
../problem010.cpp \
../problem011.cpp \
../problem012.cpp \
../problem013.cpp \
../problem014.cpp \
../problem015.cpp \
../problem016.cpp \
../problem017.cpp \
../problem018.cpp \
../problem019.cpp \
../problem020.cpp \
../problem067.cpp 

OBJS += \
./common.o \
./problem001.o \
./problem002.o \
./problem003.o \
./problem004.o \
./problem005.o \
./problem006.o \
./problem007.o \
./problem008.o \
./problem009.o \
./problem010.o \
./problem011.o \
./problem012.o \
./problem013.o \
./problem014.o \
./problem015.o \
./problem016.o \
./problem017.o \
./problem018.o \
./problem019.o \
./problem020.o \
./problem067.o 

CPP_DEPS += \
./common.d \
./problem001.d \
./problem002.d \
./problem003.d \
./problem004.d \
./problem005.d \
./problem006.d \
./problem007.d \
./problem008.d \
./problem009.d \
./problem010.d \
./problem011.d \
./problem012.d \
./problem013.d \
./problem014.d \
./problem015.d \
./problem016.d \
./problem017.d \
./problem018.d \
./problem019.d \
./problem020.d \
./problem067.d 


# Each subdirectory must supply rules for building sources it contributes
%.o: ../%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


