# Basic definitions

## Software Development

- Def'n: Breaking down big task -> managable tasks
- Props:
	- Systematic
	- Formal

## Software Process
- Waterfall
- Evolutionary prototype
- RUP
- Agile

## Software Phases
- Requirement engineering
- Design
- Implementation
- Verification & Validation
- Maintanance


# Software phases

## RE

### Def'n
- *Establish services that customer requires*
- Completeness & Pertinent: lack of requirements/ irrelevant with requirements
- Software quality: both software and purpose

| User requirement | System requirement |
|------------------|--------------------|
| for customer     | for dev            |
| no tech detail   | tech detail        |

| Func requirement    | Non-func requirement |
|---------------------|----------------------|
| What sys does       | Sys quality          |
| Have clear criteria | !Have clear criteria |


### Why important?
-> Reduce such cost!

### Source
- Stakeholder
- App domain: e.g banking regulation
- Documentation

### Analysing requirements
- Verification: check correctness, completeness & pertinent
- Validation: req is what stakeholder want?
- Risk analysis: main risk of system?

### RE prioritization
- Mandatory
- Nice to have
- Superflous

### Problems
- Have to gather from conflict, bias sources
- Hard to describe to other

### Technik
- Reading
- Hard data and samples
- Interview
- Surveys
- Meeting

### Product: SRS

## Design: TODO afternoon

## Implementation: TODO afternoon

## Verification and Validation

### Def'n
*Does we build the system rite?*

| Failure            | Fault          | Error          |
|--------------------|----------------|----------------|
| incorrect behavior | incorrect code | cause of fault |

- Black-box testing: base on description
- White-box testing: base on the code

### Approaches

|       | Testing        | Static verify | Inspection                              | Formal proof     |
|-------|----------------|---------------|-----------------------------------------|------------------|
| Def'n | idv test cases | all input     | ppl look at the code and find defects   | MAFFFFFFFFFF!    |
| Pro   | no flase alarm | complete      | systematic and through analysis of code | strong guarantee |
| Con   | incomplete     | false alarm   | informal, subjective                    | complex          |

### Testing

#### Testing level
|                     | Modules   |
|---------------------|-----------|
| Unit testing        | 1         |
| Integration testing | multiple  |
| System testing      | whole sys |

#### Alpha, Beta, Release?
```
 Dev testing	     Alpha	     	  Beta		   Release
-------------------|--------------------|----------------|------------->
 within test organ   internal set users   external set
```

### Black-box

#### Technik
- Partition testing: div I domain -> partitions (failures dense in some partitions)
- Boundary value: test boundary of domains

#### Types
- Func testing: (see RE)
- Non-func testing: (see RE)
- Regression testing: new code affects existed code?

#### Steps
1. examine the RE
2. test valid/invalid input
3. detemines expected output
4. create & execute test cases     
5. compare output with expected
6. fix & re-test

### White-box

#### Technik
**Coverage**: how much src code is tested
```
printSum(a, b)	
	result = a + b							<----- Statement
	if result > 0 or result == 9			<----- 2 Conditions	|
		print("red")											| Branch
	else
		print("blue)
```

- Statement cov
- Branch cov
- Condition cov

#### Types
- Unit testing
- Penetration testing: expose security threats
- Mutation testing: best technik for solution

#### Steps
1. learn & understand src code
2. create testcase & execute
3. fix & re-test

## Maintenance

### WHY?
- Requirements changes -> design change`
- Improve design
- STOP BEING LAZYYYY

### Types

#### Colapse hierarchy
super class & sub class are TOO similar -> merge 2 classes

#### Decompse conditionals
complex conditional statement -> make methods from conditions

e.g:
``` python
if date.before(SUMMER_START) or date.after(SUMMER_END):
	...

					|
					|
					|
					v

if not_summer(date)
	...
```

#### Extract/Inclide class 
|          | Extract class        | Incline class        |
|----------|----------------------|----------------------|
| Behavior | class doing too much | class not doing much |
| Solution | split class          | merge class          |

#### Extract method
method is too long & have cohensive segment -> create new method of that segment

### When?
- duplicated code code
- LONGG method
- LARGEEE class
- feature envy: class is calling other class's feature too much
- shotgun surgery: 1 little change cuz 1000 more little changes

### When not?
- code is broken
- no reason to refac