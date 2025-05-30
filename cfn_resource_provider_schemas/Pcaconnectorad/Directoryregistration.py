SCHEMA = {
  "typeName" : "AWS::PCAConnectorAD::DirectoryRegistration",
  "description" : "Definition of AWS::PCAConnectorAD::DirectoryRegistration Resource Type",
  "definitions" : {
    "Tags" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DirectoryId" : {
      "type" : "string",
      "pattern" : "^d-[0-9a-f]{10}$"
    },
    "DirectoryRegistrationArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:[\\w-]+:pca-connector-ad:[\\w-]+:[0-9]+:directory-registration(\\/[\\w-]+)$"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "required" : [ "DirectoryId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pca-connector-ad:ListTagsForResource", "pca-connector-ad:TagResource", "pca-connector-ad:UntagResource" ]
  },
  "readOnlyProperties" : [ "/properties/DirectoryRegistrationArn" ],
  "createOnlyProperties" : [ "/properties/DirectoryId" ],
  "primaryIdentifier" : [ "/properties/DirectoryRegistrationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ds:AuthorizeApplication", "ds:DescribeDirectories", "pca-connector-ad:GetDirectoryRegistration", "pca-connector-ad:CreateDirectoryRegistration", "pca-connector-ad:TagResource" ]
    },
    "read" : {
      "permissions" : [ "pca-connector-ad:GetDirectoryRegistration", "pca-connector-ad:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "ds:DescribeDirectories", "ds:UnauthorizeApplication", "ds:UpdateAuthorizedApplication", "pca-connector-ad:GetDirectoryRegistration", "pca-connector-ad:DeleteDirectoryRegistration", "pca-connector-ad:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "pca-connector-ad:ListDirectoryRegistrations" ]
    },
    "update" : {
      "permissions" : [ "pca-connector-ad:ListTagsForResource", "pca-connector-ad:TagResource", "pca-connector-ad:UntagResource" ]
    }
  },
  "additionalProperties" : False
}