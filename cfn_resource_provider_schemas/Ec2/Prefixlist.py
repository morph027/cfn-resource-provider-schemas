SCHEMA = {
  "typeName" : "AWS::EC2::PrefixList",
  "description" : "Resource schema of AWS::EC2::PrefixList Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "Entry" : {
      "type" : "object",
      "properties" : {
        "Cidr" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 46
        },
        "Description" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 255
        }
      },
      "required" : [ "Cidr" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "PrefixListName" : {
      "description" : "Name of Prefix List.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "PrefixListId" : {
      "description" : "Id of Prefix List.",
      "type" : "string"
    },
    "OwnerId" : {
      "description" : "Owner Id of Prefix List.",
      "type" : "string"
    },
    "AddressFamily" : {
      "description" : "Ip Version of Prefix List.",
      "type" : "string",
      "enum" : [ "IPv4", "IPv6" ]
    },
    "MaxEntries" : {
      "description" : "Max Entries of Prefix List.",
      "type" : "integer",
      "minimum" : 1
    },
    "Version" : {
      "description" : "Version of Prefix List.",
      "type" : "integer"
    },
    "Tags" : {
      "description" : "Tags for Prefix List",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Entries" : {
      "description" : "Entries of Prefix List.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Entry"
      }
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the Prefix List.",
      "type" : "string"
    }
  },
  "required" : [ "PrefixListName", "AddressFamily" ],
  "readOnlyProperties" : [ "/properties/PrefixListId", "/properties/OwnerId", "/properties/Version", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/PrefixListId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "EC2:DeleteTags", "EC2:CreateTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "EC2:CreateManagedPrefixList", "EC2:DescribeManagedPrefixLists", "EC2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "EC2:GetManagedPrefixListEntries", "EC2:DescribeManagedPrefixLists" ]
    },
    "update" : {
      "permissions" : [ "EC2:DescribeManagedPrefixLists", "EC2:GetManagedPrefixListEntries", "EC2:ModifyManagedPrefixList", "EC2:CreateTags", "EC2:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "EC2:DeleteManagedPrefixList", "EC2:DescribeManagedPrefixLists" ]
    },
    "list" : {
      "permissions" : [ "EC2:DescribeManagedPrefixLists", "EC2:GetManagedPrefixListEntries" ]
    }
  },
  "additionalProperties" : False
}