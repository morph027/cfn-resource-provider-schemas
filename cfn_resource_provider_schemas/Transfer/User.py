SCHEMA = {
  "typeName" : "AWS::Transfer::User",
  "description" : "Definition of AWS::Transfer::User Resource Type",
  "definitions" : {
    "HomeDirectoryMapEntry" : {
      "type" : "object",
      "properties" : {
        "Entry" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 0,
          "pattern" : "^/.*$"
        },
        "Target" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 0,
          "pattern" : "^/.*$"
        },
        "Type" : {
          "$ref" : "#/definitions/MapType"
        }
      },
      "required" : [ "Entry", "Target" ],
      "additionalProperties" : False
    },
    "HomeDirectoryType" : {
      "type" : "string",
      "enum" : [ "PATH", "LOGICAL" ]
    },
    "MapType" : {
      "type" : "string",
      "enum" : [ "FILE", "DIRECTORY" ]
    },
    "PosixProfile" : {
      "type" : "object",
      "properties" : {
        "Uid" : {
          "type" : "number",
          "maximum" : 4294967295,
          "minimum" : 0
        },
        "Gid" : {
          "type" : "number",
          "maximum" : 4294967295,
          "minimum" : 0
        },
        "SecondaryGids" : {
          "type" : "array",
          "insertionOrder" : False,
          "items" : {
            "type" : "number",
            "maximum" : 4294967295,
            "minimum" : 0
          },
          "maxItems" : 16,
          "minItems" : 0
        }
      },
      "required" : [ "Gid", "Uid" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 0
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 20,
      "pattern" : "^arn:\\S+$"
    },
    "HomeDirectory" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0,
      "pattern" : "^(|/.*)$"
    },
    "HomeDirectoryMappings" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/HomeDirectoryMapEntry"
      },
      "maxItems" : 50000,
      "minItems" : 1
    },
    "HomeDirectoryType" : {
      "$ref" : "#/definitions/HomeDirectoryType"
    },
    "Policy" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 0
    },
    "PosixProfile" : {
      "$ref" : "#/definitions/PosixProfile"
    },
    "Role" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:.*role/\\S+$"
    },
    "ServerId" : {
      "type" : "string",
      "maxLength" : 19,
      "minLength" : 19,
      "pattern" : "^s-([0-9a-f]{17})$"
    },
    "SshPublicKeys" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "minLength" : 0,
        "pattern" : "^\\s*(ssh|ecdsa)-[a-z0-9-]+[ \\t]+(([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{1,3})?(={0,3})?)(\\s*|[ \\t]+[\\S \\t]*\\s*)$"
      },
      "description" : "This represents the SSH User Public Keys for CloudFormation resource"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50,
      "minItems" : 1
    },
    "UserName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 3,
      "pattern" : "^[\\w][\\w@.-]{2,99}$"
    }
  },
  "required" : [ "Role", "ServerId", "UserName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/ServerId", "/properties/UserName" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/ServerId", "/properties/UserName" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "transfer:CreateUser", "transfer:DescribeUser", "transfer:ImportSshPublicKey", "transfer:TagResource" ]
    },
    "read" : {
      "permissions" : [ "transfer:DescribeUser" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "transfer:DeleteSshPublicKey", "transfer:DescribeUser", "transfer:ImportSshPublicKey", "transfer:TagResource", "transfer:UnTagResource", "transfer:UpdateUser" ]
    },
    "delete" : {
      "permissions" : [ "transfer:DeleteUser" ]
    },
    "list" : {
      "permissions" : [ "transfer:ListUsers" ],
      "handlerSchema" : {
        "properties" : {
          "ServerId" : {
            "$ref" : "resource-schema.json#/properties/ServerId"
          }
        },
        "required" : [ "ServerId" ]
      }
    }
  },
  "tagging" : {
    "cloudFormationSystemTags" : True,
    "permissions" : [ "transfer:TagResource", "transfer:UnTagResource", "transfer:ListTagsForResource" ],
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True
  },
  "additionalProperties" : False,
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-transfer"
}