SCHEMA = {
  "typeName" : "AWS::CodeStarConnections::RepositoryLink",
  "description" : "Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codestarconnections.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, , ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, , ., /, =, +, and -. ",
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
      "description" : "The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):.+:.+:[0-9]{12}:.+"
    },
    "ProviderType" : {
      "description" : "The name of the external provider where your third-party code repository is configured.",
      "type" : "string",
      "enum" : [ "GitHub", "Bitbucket", "GitHubEnterprise", "GitLab", "GitLabSelfManaged" ]
    },
    "OwnerId" : {
      "description" : "the ID of the entity that owns the repository.",
      "type" : "string",
      "pattern" : "[a-za-z0-9_\\.-]+"
    },
    "RepositoryName" : {
      "description" : "The repository for which the link is being created.",
      "type" : "string",
      "pattern" : "[a-za-z0-9_\\.-]+"
    },
    "EncryptionKeyArn" : {
      "description" : "The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):.+:.+:[0-9]{12}:.+"
    },
    "RepositoryLinkId" : {
      "description" : "A UUID that uniquely identifies the RepositoryLink.",
      "type" : "string",
      "pattern" : "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    },
    "RepositoryLinkArn" : {
      "description" : "A unique Amazon Resource Name (ARN) to designate the repository link.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):.+:.+:[0-9]{12}:.+"
    },
    "Tags" : {
      "description" : "Specifies the tags applied to a RepositoryLink.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "RepositoryName", "ConnectionArn", "OwnerId" ],
  "createOnlyProperties" : [ "/properties/RepositoryName", "/properties/OwnerId" ],
  "readOnlyProperties" : [ "/properties/RepositoryLinkArn", "/properties/RepositoryLinkId", "/properties/ProviderType" ],
  "primaryIdentifier" : [ "/properties/RepositoryLinkArn" ],
  "additionalIdentifiers" : [ [ "/properties/RepositoryLinkId" ] ],
  "handlers" : {
    "update" : {
      "permissions" : [ "codestar-connections:GetConnection", "codestar-connections:ListTagsForResource", "codestar-connections:PassConnection", "codestar-connections:UseConnection", "codestar-connections:TagResource", "codestar-connections:UntagResource", "codestar-connections:UpdateRepositoryLink" ]
    },
    "create" : {
      "permissions" : [ "codestar-connections:CreateRepositoryLink", "codestar-connections:TagResource", "codestar-connections:UseConnection", "codestar-connections:PassConnection", "codestar-connections:GetConnection", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "codestar-connections:GetRepositoryLink", "codestar-connections:ListTagsForResource", "codestar-connections:GetConnection" ]
    },
    "delete" : {
      "permissions" : [ "codestar-connections:GetRepositoryLink", "codestar-connections:DeleteRepositoryLink", "codestar-connections:GetConnection" ]
    },
    "list" : {
      "permissions" : [ "codestar-connections:ListRepositoryLinks", "codestar-connections:ListTagsForResource" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "codestar-connections:UntagResource", "codestar-connections:ListTagsForResource", "codestar-connections:TagResource" ]
  },
  "additionalProperties" : False
}