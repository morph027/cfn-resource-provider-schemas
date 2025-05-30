SCHEMA = {
  "typeName" : "AWS::Route53Profiles::ProfileAssociation",
  "description" : "Resource Type definition for AWS::Route53Profiles::ProfileAssociation",
  "additionalProperties" : False,
  "properties" : {
    "ResourceId" : {
      "description" : "The resource that you associated the  profile with.",
      "type" : "string"
    },
    "ProfileId" : {
      "description" : "The ID of the  profile that you associated with the resource that is specified by ResourceId.",
      "type" : "string"
    },
    "Id" : {
      "description" : "Primary Identifier for  Profile Association",
      "type" : "string"
    },
    "Name" : {
      "description" : "The name of an association between a  Profile and a VPC.",
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "description" : "An array of key-value pairs to apply to this resource.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the profile association."
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
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
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "ResourceId", "ProfileId", "Name" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "writeOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/ResourceId", "/properties/ProfileId" ],
  "replacementStrategy" : "delete_then_create",
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "route53profiles:TagResource", "route53profiles:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "route53profiles:AssociateProfile", "route53profiles:GetProfileAssociation", "route53profiles:ListProfileAssociations", "ec2:DescribeVpcs", "route53profiles:TagResource", "route53profiles:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "route53profiles:GetProfileAssociation", "route53profiles:TagResource", "route53profiles:UntagResource", "route53profiles:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "route53profiles:GetProfileAssociation", "route53profiles:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "route53profiles:DisassociateProfile", "route53profiles:GetProfileAssociation", "route53profiles:UntagResource", "route53profiles:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "route53profiles:ListProfileAssociations", "route53profiles:ListTagsForResource" ]
    }
  }
}