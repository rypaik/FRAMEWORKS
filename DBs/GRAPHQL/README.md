## SCHEMA



type Person { 
    name: String!
    age: Int!
}


type Post { 
    title: String!
}



### Relationships

type Person { 
    name: String!
    age: Int!
    posts: [Post!]!
}

#### author links to posts in Person Schema
type Post { 
    title: String!
    author: Person!
}




### Queries

#query
{ 
    allPersons {
        name
    }
}


#response
{
    "allPersons": [
       {"name": "Johnny"},
       {"name": "Sarah"},
       {"name": "Alice} 
    ]
}



#query
{
    allPersons {
        name
        age
    }
}

#responses
{ 
    "allPersons": [
        {"name": "Johnny", "age":23},
        {"name": "Sarah", "age": 20},
        {"name": "Alice, "age": 20} 
    ]
}



##### -----------------
Sample Queries

{ 
    allPersons(last:2) { 
        name
        age
    }
}

{
    allPersons {
        name
            posts {
                title
            }
    }
}




## MUTATIONS
create new data
update existing data
delete existing data


#create

mutation {
    createPerson(name: "Bob", age:36) {
        name
        age
    }
}

#querying
{
    "createPerson": {
        "name": "Bob",
        "age": 36,
    }
}


### Schema 
type Person{
    id: ID!
    name: String!
    age: Int!
}


# extending data
mutation { 
    createPerson(name:"Bob"m age: 36) {
        id
    }
}






##### ------ 
Subscriptions - Real Time updates

subscription{
    newPerson{
        name
        age
    }
}




## SCHEMA


#root types
type Query {
    ...
}

type Mutation {
    ...
}


type Subscription {
    ...
}


### DEFINING SCHEMA
#Query type

## Full Query
type Person {
    id: ID!
    name: String!
    age: Int!
    posts: [Posts!]!
}

type Post{
    title: String!
    author: Person!
}

type Query { 
    allPersons(last:Int): [Person!]!
    allPosts(last:Int) : [Post!]!
}

type Mutation {
    createPerson(name: String!, age: String!): Person!
    updatePerson(id: ID!, name: String!, age: String!): Person!
    deletePerson(id: ID!): Person!
}

type Subscription {
    newPerson: Person!
}

##END OF FULL QUERY

{ 
    allPersons{
        name
    }
}

type Query { 
    allPersons(last:Int): [Person!]!
}


#mutation type

#call
mutation{
    createPerson(name:"Bob", age: 36) {
        id
    }
}

# schema declaration
type Mutation {
    createPerson(name: String!, age: String!): Person!
}


subscription {
    newPerson {
        name
        age
    }
}

type Subscription {
    newPerson: Person!
}