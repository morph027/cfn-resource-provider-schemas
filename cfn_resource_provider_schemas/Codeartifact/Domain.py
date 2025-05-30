SCHEMA = {
  "typeName" : "AWS::CodeArtifact::Domain",
  "description" : "The resource schema to create a CodeArtifact domain.",
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
    "DomainName" : {
      "description" : "The name of the domain.",
      "type" : "string",
      "pattern" : "^([a-z][a-z0-9\\-]{0,48}[a-z0-9])$",
      "minLength" : 2,
      "maxLength" : 50
    },
    "Name" : {
      "description" : "The name of the domain. This field is used for GetAtt",
      "type" : "string",
      "pattern" : "^([a-z][a-z0-9\\-]{0,48}[a-z0-9])$",
      "minLength" : 2,
      "maxLength" : 50
    },
    "Owner" : {
      "description" : "The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt",
      "pattern" : "[0-9]{12}",
      "type" : "string"
    },
    "EncryptionKey" : {
      "description" : "The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.",
      "type" : "string"
    },
    "PermissionsPolicyDocument" : {
      "description" : "The access control resource policy on the provided domain.",
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
    },
    "Arn" : {
      "description" : "The ARN of the domain.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    }
  },
  "additionalProperties" : False,
  "required" : [ "DomainName" ],
  "createOnlyProperties" : [ "/properties/DomainName", "/properties/EncryptionKey" ],
  "readOnlyProperties" : [ "/properties/Owner", "/properties/Name", "/properties/EncryptionKey", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codeartifact:CreateDomain", "codeartifact:DescribeDomain", "codeartifact:PutDomainPermissionsPolicy", "codeartifact:GetDomainPermissionsPolicy", "codeartifact:TagResource", "codeartifact:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "codeartifact:DescribeDomain", "codeartifact:GetDomainPermissionsPolicy", "codeartifact:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "codeartifact:DescribeDomain", "codeartifact:PutDomainPermissionsPolicy", "codeartifact:DeleteDomainPermissionsPolicy", "codeartifact:GetDomainPermissionsPolicy", "codeartifact:TagResource", "codeartifact:UntagResource", "codeartifact:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "codeartifact:DeleteDomain", "codeartifact:DescribeDomain" ]
    },
    "list" : {
      "permissions" : [ "codeartifact:ListDomains" ]
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