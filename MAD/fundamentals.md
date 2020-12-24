# Architecture
- Linux kernel: très bien
- Lib + Android run time (C): provide local DB, lower level framework
- App framework (Java, Kotlin): higher lvl framework, UI
- Apps (Java, Kotlin)

# Source -> Device
Java/Kotlin src code -> Java Byte Code -> Dalvik Byte Code (optimize for phones: memory, slow)

# Android Virtual Machine
- Dalvik: translate online
- ART(Android RunTime): translate prev offline

# MVC Model
- model: sth to store objects
- view: show and let user to interact
- controller: control the whole sys

# Application
- global data
- early init of libs
- android mem management
  - garbage collector
  - upper limit ea app
  - kill activities when low on mem
  - out-of-mem exception
  

# Activity
- fundamental building block
- has unique tasks
- handle display of a single screen
- life cycle

```
									   onResume()			onPause()
									 +-----------> Resumed -------------+
					   onStart()	 |					^			 	v
					+-----------> Started				+----------- Paused ----------+
					|				^					 onResume() 		 onStop() v
	+----------> Created			+---------------------------------------------- Stoped ---------+
	|											onRestart()									onDes()	v
onCreate()																						Destroyed
```

# Fragments
- fragment: control parts of UI
- similar lifecycle:
  - onCreate(): init
  - onCreateView(): view init
  - onPause(): user leaves
  
# Note
- mid: offline, fake data
- fin: online, real model
- phone: small screen, touch/swipe a lot

# View
## TextView
- drawable: icons (align w/ textview)
- gravity: align textview
- styles: css
## ImageVIew

