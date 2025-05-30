SCHEMA = {
  "typeName" : "AWS::CodeStarConnections::Connection",
  "description" : "Schema for AWS::CodeStarConnections::Connection resource which can be used to connect external source providers with AWS CodePipeline",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codestarconnections.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ConnectionArn" : {
      "description" : "The Amazon Resource Name (ARN) of the  connection. The ARN is used as the connection reference when the connection is shared between AWS services.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 256,
      "pattern" : "arn:aws(-[\\w]+)*:.+:.+:[0-9]{12}:.+"
    },
    "ConnectionName" : {
      "description" : "The name of the connection. Connection names must be unique in an AWS user account.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 32
    },
    "ConnectionStatus" : {
      "description" : "The current status of the connection.",
      "type" : "string"
    },
    "OwnerAccountId" : {
      "description" : "The name of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.",
      "type" : "string",
      "minLength" : 12,
      "maxLength" : 12,
      "pattern" : "[0-9]{12}"
    },
    "ProviderType" : {
      "description" : "The name of the external provider where your third-party code repository is configured. You must specify either a ProviderType or a HostArn.",
      "type" : "string"
    },
    "HostArn" : {
      "description" : "The host arn configured to represent the infrastructure where your third-party provider is installed. You must specify either a ProviderType or a HostArn.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 256,
      "pattern" : "arn:aws(-[\\w]+)*:.+:.+:[0-9]{12}:.+"
    },
    "Tags" : {
      "description" : "Specifies the tags applied to a connection.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False
    }
  },
  "required" : [ "ConnectionName" ],
  "createOnlyProperties" : [ "/properties/ConnectionName", "/properties/ProviderType", "/properties/HostArn" ],
  "readOnlyProperties" : [ "/properties/ConnectionArn", "/properties/ConnectionStatus", "/properties/OwnerAccountId" ],
  "primaryIdentifier" : [ "/properties/ConnectionArn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "codestar-connections:TagResource", "codestar-connections:ListTagsForResource", "codestar-connections:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "codestar-connections:CreateConnection", "codestar-connections:TagResource" ]
    },
    "read" : {
      "permissions" : [ "codestar-connections:GetConnection", "codestar-connections:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "codestar-connections:ListTagsForResource", "codestar-connections:TagResource", "codestar-connections:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "codestar-connections:DeleteConnection" ]
    },
    "list" : {
      "permissions" : [ "codestar-connections:ListConnections", "codestar-connections:ListTagsForResource" ]
    }
  },
  "additionalProperties" : False
}