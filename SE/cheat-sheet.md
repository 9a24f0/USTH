# Basic definitions

## Software Development

- Def'n: Breaking down big task -> managable tasks
- Props:
	- Systematic
	- Formal

## Software Process
- [Waterfall](#Waterfall)
- [Evolutionary prototype](#Evolutionary\ prototyping)
- [RUP](#RUP)
- [Agile](#Agile)

## Software Phases
- [Requirement engineering](#RE)
- [Design](#Design)
- Implementation
- [Verification & Validation](#Verification\ and\ Validation)
- [Maintenance](#Maintenance)


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

## Design

### Def'n
- Software Architecture (SWA): blueprint of software system (involve: structure, behavior, internal interaction, non-func props)
- Temporal aspect: design changes over time

| Prescriptive (as-conceived)    | Descriptive (as-implemented) |
|--------------------------------|------------------------------|
| dictates how sys will be build | how sys actually built       |

| Drift                                 | Erosion                           |
|---------------------------------------|-----------------------------------|
| changes that not violate architecture | changes that violate architecture |
| lead to unecessary complex            | lead to poor architecture design  |

### Elements
```
	+---------------------+			 +--------------+					+------------+
	| processing elements |		+	 | data element |    ---------->    | components |
	+---------------------+			 +--------------+					+------------+

	+------------+			 +----------------------+					+-------------------+
	| components |     +     | interaction elements |	 ---------->	| sys configuration |
	+------------+			 +----------------------+					+-------------------+
```

### Types of architecture
- Pipe and filters: output of A -> input of B
- Event driven: event + event consumer
- Publish and subscribe: twitter
- Client-server: email
- P2P: ea peer acts as supplier and consumer of resources
- REST(representational state transfer)

### Design pattern

#### Factory method pattern
make a factory method (abstract method for creating instances)

#### Strategy pattern: TODO

## Implementation

## Verification and Validation

### Def'n
*Verify: Does we build the system rite?*

*Validate: Does we build the rite system?*

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

# Software Process

## Waterfall
```
+----------+
| Software |_____
| concept  |	|
+----------+	|
				|
			+-------------+
			| Requirement |______
			| analysis	  |		|
			+-------------+		|
								|
							+---------------+
							| Architectural |________
							| design		|		|
							+---------------+		|
													|
												+----------+
												| Detailed |_________ 
												| design   |		|
												+----------+		|
																	|
																+------------+
																| Coding and |_______
																| debugging  |		|
																+------------+		|
																					|
																				+---------+
																				| System  |
																				| testing |
																				+---------+
```
- Pro: find errors early
- Con: diff to change

## Evolutionary prototyping
design intial prototype -> refine -> complete release prototype

- Pro: immediate feedback
- Con: diff to plan

## RUP
- RUP defines:
  - order of phases
  - transition criteria
- Base of components

### Distinguishing aspect
- Use-case driven: what sys do for ea user?
- Architecture-centric
- Interative & incremental: life time consist of cycles (1 cycles have all phases)

### Phases

| Phases       | Goals                                                          | Outcome                                                  |
|--------------|----------------------------------------------------------------|----------------------------------------------------------|
| Inception    | idea -> vision of end product                                  | initial use-case model, project plan & risk assesment    |
| Elaboration  | analyses problem, establish arch, eliminate risks, refine plan | use-case model, sup requirements, architecture           |
| Construction | features developed & tested                                    | complet product, test results, user manual               |
| Transition   | new release                                                    | completed project, usable product, plan for next release |

## Agile: TODO