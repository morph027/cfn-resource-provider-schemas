SCHEMA = {
  "typeName" : "AWS::CodeArtifact::Repository",
  "description" : "The resource schema to create a CodeArtifact repository.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codeartifact",
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
          "description" : "The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "RepositoryName" : {
      "description" : "The name of the repository.",
      "type" : "string",
      "pattern" : "^([A-Za-z0-9][A-Za-z0-9._\\-]{1,99})$",
      "minLength" : 2,
      "maxLength" : 100
    },
    "Name" : {
      "description" : "The name of the repository. This is used for GetAtt",
      "type" : "string",
      "pattern" : "^([A-Za-z0-9][A-Za-z0-9._\\-]{1,99})$",
      "minLength" : 2,
      "maxLength" : 100
    },
    "DomainName" : {
      "description" : "The name of the domain that contains the repository.",
      "type" : "string",
      "pattern" : "^([a-z][a-z0-9\\-]{0,48}[a-z0-9])$",
      "minLength" : 2,
      "maxLength" : 50
    },
    "DomainOwner" : {
      "description" : "The 12-digit account ID of the AWS account that owns the domain.",
      "pattern" : "[0-9]{12}",
      "type" : "string"
    },
    "Description" : {
      "description" : "A text description of the repository.",
      "type" : "string",
      "maxLength" : 1000
    },
    "Arn" : {
      "description" : "The ARN of the repository.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "ExternalConnections" : {
      "description" : "A list of external connections associated with the repository.",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "Upstreams" : {
      "description" : "A list of upstream repositories associated with the repository.",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "PermissionsPolicyDocument" : {
      "description" : "The access control resource policy on the provided repository.",
      "type" : "object",
      "minLength" : 2,
      "maxLength" : 5120
    },
    "Tags" : {
      "type" : "array",
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "RepositoryName", "DomainName" ],
  "createOnlyProperties" : [ "/properties/RepositoryName", "/properties/DomainName", "/properties/DomainOwner" ],
  "readOnlyProperties" : [ "/properties/Name", "/properties/DomainOwner", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codeartifact:CreateRepository", "codeartifact:DescribeRepository", "codeartifact:PutRepositoryPermissionsPolicy", "codeartifact:GetRepositoryPermissionsPolicy", "codeartifact:AssociateExternalConnection", "codeartifact:AssociateWithDownstreamRepository", "codeartifact:TagResource", "codeartifact:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "codeartifact:DescribeRepository", "codeartifact:GetRepositoryPermissionsPolicy", "codeartifact:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "codeartifact:PutRepositoryPermissionsPolicy", "codeartifact:GetRepositoryPermissionsPolicy", "codeartifact:DeleteRepositoryPermissionsPolicy", "codeartifact:AssociateExternalConnection", "codeartifact:DisassociateExternalConnection", "codeartifact:UpdateRepository", "codeartifact:DescribeRepository", "codeartifact:AssociateWithDownstreamRepository", "codeartifact:TagResource", "codeartifact:UntagResource", "codeartifact:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "codeartifact:DeleteRepository", "codeartifact:DescribeRepository" ]
    },
    "list" : {
      "permissions" : [ "codeartifact:ListRepositories" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "codeartifact:ListTagsForResource", "codeartifact:UntagResource", "codeartifact:TagResource" ]
  }
}