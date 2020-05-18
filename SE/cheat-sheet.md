# Basic definitions

## Software Development:

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


# Software phases:

## RE

### Def'n:
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

### Source:
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

### Problems:
- Have to gather from conflict, bias sources
- Hard to describe to other

### Technik:
- Reading
- Hard data and samples
- Interview
- Surveys
- Meeting

### Product: SRS

## Design: TODO afternoon

## Implementation: TODO afternoon

## Verification and Validation

### Def'n:
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

### Black-box:

#### How?
- Partition testing: div I domain -> partitions (failures dense in some partitions)

- Boundary value: test boundary of domains
### White-bos: TODO morning
