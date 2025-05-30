SCHEMA = {
  "typeName" : "AWS::SupportApp::AccountAlias",
  "description" : "An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-supportapp.git",
  "properties" : {
    "AccountAlias" : {
      "description" : "An account alias associated with a customer's account.",
      "type" : "string",
      "pattern" : "^[\\w\\- ]+$",
      "minLength" : 1,
      "maxLength" : 30
    },
    "AccountAliasResourceId" : {
      "description" : "Unique identifier representing an alias tied to an account",
      "type" : "string",
      "pattern" : "^[\\w\\- ]+$",
      "minLength" : 29,
      "maxLength" : 29
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/AccountAliasResourceId" ],
  "required" : [ "AccountAlias" ],
  "readOnlyProperties" : [ "/properties/AccountAliasResourceId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "supportapp:PutAccountAlias", "supportapp:GetAccountAlias" ]
    },
    "read" : {
      "permissions" : [ "supportapp:GetAccountAlias" ]
    },
    "update" : {
      "permissions" : [ "supportapp:PutAccountAlias", "supportapp:GetAccountAlias" ]
    },
    "delete" : {
      "permissions" : [ "supportapp:DeleteAccountAlias", "supportapp:GetAccountAlias" ]
    },
    "list" : {
      "permissions" : [ "supportapp:GetAccountAlias" ]
    }
  }
}