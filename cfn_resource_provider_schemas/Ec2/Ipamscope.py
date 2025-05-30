SCHEMA = {
  "typeName" : "AWS::EC2::IPAMScope",
  "description" : "Resource Schema of AWS::EC2::IPAMScope Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ipam.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "IpamScopeId" : {
      "description" : "Id of the IPAM scope.",
      "type" : "string"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the IPAM scope.",
      "type" : "string"
    },
    "IpamId" : {
      "description" : "The Id of the IPAM this scope is a part of.",
      "type" : "string"
    },
    "IpamArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IPAM this scope is a part of.",
      "type" : "string"
    },
    "IpamScopeType" : {
      "description" : "Determines whether this scope contains publicly routable space or space for a private network",
      "type" : "string",
      "enum" : [ "public", "private" ]
    },
    "IsDefault" : {
      "description" : "Is this one of the default scopes created with the IPAM.",
      "type" : "boolean"
    },
    "Description" : {
      "type" : "string"
    },
    "PoolCount" : {
      "description" : "The number of pools that currently exist in this scope.",
      "type" : "integer"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "IpamId" ],
  "primaryIdentifier" : [ "/properties/IpamScopeId" ],
  "readOnlyProperties" : [ "/properties/IpamScopeId", "/properties/Arn", "/properties/IpamArn", "/properties/IsDefault", "/properties/PoolCount", "/properties/IpamScopeType" ],
  "createOnlyProperties" : [ "/properties/IpamId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateIpamScope", "ec2:DescribeIpamScopes", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeIpamScopes" ]
    },
    "update" : {
      "permissions" : [ "ec2:ModifyIpamScope", "ec2:DescribeIpamScopes", "ec2:CreateTags", "ec2:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteIpamScope", "ec2:DescribeIpamScopes", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeIpamScopes" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:DeleteTags", "ec2:CreateTags" ]
  }
}