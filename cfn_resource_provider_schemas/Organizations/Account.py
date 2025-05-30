SCHEMA = {
  "typeName" : "AWS::Organizations::Account",
  "description" : "You can use AWS::Organizations::Account to manage accounts in organization.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-organizations",
  "properties" : {
    "AccountName" : {
      "description" : "The friendly name of the member account.",
      "type" : "string",
      "pattern" : "[\\u0020-\\u007E]+",
      "minLength" : 1,
      "maxLength" : 50
    },
    "Email" : {
      "description" : "The email address of the owner to assign to the new member account.",
      "type" : "string",
      "pattern" : "[^\\s@]+@[^\\s@]+\\.[^\\s@]+",
      "minLength" : 6,
      "maxLength" : 64
    },
    "RoleName" : {
      "description" : "The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.",
      "type" : "string",
      "default" : "OrganizationAccountAccessRole",
      "pattern" : "[\\w+=,.@-]{1,64}",
      "minLength" : 1,
      "maxLength" : 64
    },
    "ParentIds" : {
      "description" : "List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "type" : "string",
        "pattern" : "^(r-[0-9a-z]{4,32})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$"
      }
    },
    "Tags" : {
      "description" : "A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "AccountId" : {
      "description" : "If the account was created successfully, the unique identifier (ID) of the new account.",
      "type" : "string",
      "pattern" : "^\\d{12}$",
      "maxLength" : 12
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the account.",
      "type" : "string",
      "pattern" : "^arn:aws.*:organizations::\\d{12}:account\\/o-[a-z0-9]{10,32}\\/\\d{12}"
    },
    "JoinedMethod" : {
      "description" : "The method by which the account joined the organization.",
      "type" : "string",
      "enum" : [ "INVITED", "CREATED" ]
    },
    "JoinedTimestamp" : {
      "description" : "The date the account became a part of the organization.",
      "type" : "string"
    },
    "Status" : {
      "description" : "The status of the account in the organization.",
      "type" : "string",
      "enum" : [ "ACTIVE", "SUSPENDED", "PENDING_CLOSURE" ]
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A custom key-value pair associated with a resource within your organization.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "The key identifier, or name, of the tag.",
          "type" : "string",
          "pattern" : "[\\s\\S]*",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to None.",
          "type" : "string",
          "pattern" : "[\\s\\S]*",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "organizations:TagResource", "organizations:UntagResource", "organizations:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "AccountName", "Email" ],
  "readOnlyProperties" : [ "/properties/AccountId", "/properties/Status", "/properties/JoinedTimestamp", "/properties/JoinedMethod", "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/RoleName" ],
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "organizations:CreateAccount", "organizations:DescribeCreateAccountStatus", "organizations:MoveAccount", "organizations:ListAccounts", "organizations:ListParents", "organizations:TagResource", "organizations:DescribeAccount", "organizations:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "organizations:DescribeAccount", "organizations:ListParents", "organizations:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "organizations:MoveAccount", "organizations:TagResource", "organizations:UntagResource", "organizations:ListRoots", "organizations:DescribeAccount", "organizations:ListParents", "organizations:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "organizations:CloseAccount" ]
    },
    "list" : {
      "permissions" : [ "organizations:ListAccounts" ]
    }
  }
}