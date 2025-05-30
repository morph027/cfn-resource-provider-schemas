SCHEMA = {
  "typeName" : "AWS::S3::AccessGrant",
  "description" : "The AWS::S3::AccessGrant resource is an Amazon S3 resource type representing permissions to a specific S3 bucket or prefix hosted in an S3 Access Grants instance.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Grantee" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "GranteeType" : {
          "description" : "Configures the transfer acceleration state for an Amazon S3 bucket.",
          "type" : "string",
          "enum" : [ "IAM", "DIRECTORY_USER", "DIRECTORY_GROUP" ]
        },
        "GranteeIdentifier" : {
          "description" : "The unique identifier of the Grantee",
          "type" : "string"
        }
      },
      "required" : [ "GranteeType", "GranteeIdentifier" ]
    },
    "AccessGrantsLocationConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3SubPrefix" : {
          "description" : "The S3 sub prefix of a registered location in your S3 Access Grants instance",
          "type" : "string"
        }
      },
      "required" : [ "S3SubPrefix" ]
    },
    "AccessGrantArn" : {
      "description" : "the Amazon Resource Name (ARN) of the specified access grant.",
      "type" : "string"
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "AccessGrantId" : {
      "description" : "The ID assigned to this access grant.",
      "type" : "string",
      "examples" : [ "7c89cbd1-0f4e-40e3-861d-afb906952b77" ]
    },
    "AccessGrantsLocationId" : {
      "description" : "The custom S3 location to be accessed by the grantee",
      "type" : "string",
      "examples" : [ "125f332b-a499-4eb6-806f-8a6a1aa4cb96" ]
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Permission" : {
      "description" : "The level of access to be afforded to the grantee",
      "type" : "string",
      "enum" : [ "READ", "WRITE", "READWRITE" ]
    },
    "ApplicationArn" : {
      "description" : "The ARN of the application grantees will use to access the location",
      "type" : "string"
    },
    "S3PrefixType" : {
      "description" : "The type of S3SubPrefix.",
      "type" : "string",
      "enum" : [ "Object" ]
    },
    "GrantScope" : {
      "description" : "The S3 path of the data to which you are granting access. It is a combination of the S3 path of the registered location and the subprefix.",
      "type" : "string"
    },
    "AccessGrantArn" : {
      "$ref" : "#/definitions/AccessGrantArn",
      "description" : "The Amazon Resource Name (ARN) of the specified access grant.",
      "examples" : [ "arn:aws:s3:us-east-2:111122223333:access-grants/default/grant/7c89cbd1-0f4e-40e3-861d-afb906952b77" ]
    },
    "Grantee" : {
      "$ref" : "#/definitions/Grantee",
      "description" : "The principal who will be granted permission to access S3."
    },
    "AccessGrantsLocationConfiguration" : {
      "$ref" : "#/definitions/AccessGrantsLocationConfiguration",
      "description" : "The configuration options of the grant location, which is the S3 path to the data to which you are granting access."
    }
  },
  "required" : [ "Grantee", "Permission", "AccessGrantsLocationId" ],
  "createOnlyProperties" : [ "/properties/S3PrefixType", "/properties/Tags" ],
  "writeOnlyProperties" : [ "/properties/S3PrefixType" ],
  "readOnlyProperties" : [ "/properties/AccessGrantId", "/properties/AccessGrantArn", "/properties/GrantScope" ],
  "primaryIdentifier" : [ "/properties/AccessGrantId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "s3:UntagResource", "s3:TagResource", "s3:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:CreateAccessGrant", "s3:TagResource" ]
    },
    "read" : {
      "permissions" : [ "s3:GetAccessGrant", "s3:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteAccessGrant" ]
    },
    "list" : {
      "permissions" : [ "s3:ListAccessGrants" ]
    },
    "update" : {
      "permissions" : [ "s3:TagResource", "s3:UntagResource" ]
    }
  },
  "additionalProperties" : False
}