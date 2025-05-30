SCHEMA = {
  "typeName" : "AWS::S3::AccessGrantsLocation",
  "description" : "The AWS::S3::AccessGrantsLocation resource is an Amazon S3 resource type hosted in an access grants instance which can be the target of S3 access grants.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3",
  "definitions" : {
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
    "AccessGrantsLocationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the specified Access Grants location.",
      "type" : "string",
      "examples" : [ "arn:aws:s3:us-east-2:479290226168:access-grants/default/location/125f332b-a499-4eb6-806f-8a6a1aa4cb96" ]
    },
    "AccessGrantsLocationId" : {
      "type" : "string",
      "description" : "The unique identifier for the specified Access Grants location."
    },
    "IamRoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of the access grant location's associated IAM role.",
      "type" : "string",
      "examples" : [ "arn:aws:iamw::123456789012:role/rolename" ]
    },
    "LocationScope" : {
      "type" : "string",
      "description" : "Descriptor for where the location actually points",
      "examples" : [ "s3://test-bucket-access-grants-cmh/prefixA" ]
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/AccessGrantsLocationArn", "/properties/AccessGrantsLocationId" ],
  "primaryIdentifier" : [ "/properties/AccessGrantsLocationId" ],
  "createOnlyProperties" : [ "/properties/Tags" ],
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
      "permissions" : [ "s3:CreateAccessGrantsLocation", "iam:PassRole", "s3:TagResource" ]
    },
    "read" : {
      "permissions" : [ "s3:GetAccessGrantsLocation", "s3:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteAccessGrantsLocation" ]
    },
    "list" : {
      "permissions" : [ "s3:ListAccessGrantsLocations" ]
    },
    "update" : {
      "permissions" : [ "s3:UpdateAccessGrantsLocation", "s3:TagResource", "s3:UntagResource", "iam:PassRole" ]
    }
  },
  "additionalProperties" : False
}