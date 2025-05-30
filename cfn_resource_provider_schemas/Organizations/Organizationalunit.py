SCHEMA = {
  "typeName" : "AWS::Organizations::OrganizationalUnit",
  "description" : "You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-organizations",
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of this OU.",
      "type" : "string",
      "pattern" : "^arn:aws.*:organizations::\\d{12}:ou/o-[a-z0-9]{10,32}/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}"
    },
    "Id" : {
      "description" : "The unique identifier (ID) associated with this OU.",
      "type" : "string",
      "pattern" : "^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$",
      "maxLength" : 68
    },
    "Name" : {
      "description" : "The friendly name of this OU.",
      "type" : "string",
      "pattern" : "[\\s\\S]*",
      "minLength" : 1,
      "maxLength" : 128
    },
    "ParentId" : {
      "description" : "The unique identifier (ID) of the parent root or OU that you want to create the new OU in.",
      "type" : "string",
      "pattern" : "^(r-[0-9a-z]{4,32})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$",
      "maxLength" : 100
    },
    "Tags" : {
      "description" : "A list of tags that you want to attach to the newly created OU.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A custom key-value pair associated with a resource within your organization.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key identifier, or name, of the tag.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The string value that's associated with the key of the tag. You can set the value of a tag to an empty string, but you can't set the value of a tag to None.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "organizations:CreateOrganizationalUnit", "organizations:DescribeOrganizationalUnit", "organizations:ListParents", "organizations:ListOrganizationalUnitsForParent", "organizations:ListTagsForResource", "organizations:TagResource" ]
    },
    "read" : {
      "permissions" : [ "organizations:DescribeOrganizationalUnit", "organizations:ListParents", "organizations:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "organizations:DescribeOrganizationalUnit", "organizations:ListParents", "organizations:ListTagsForResource", "organizations:TagResource", "organizations:UntagResource", "organizations:UpdateOrganizationalUnit" ]
    },
    "delete" : {
      "permissions" : [ "organizations:DeleteOrganizationalUnit" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ParentId" : {
            "$ref" : "resource-schema.json#/properties/ParentId"
          }
        },
        "required" : [ "ParentId" ]
      },
      "permissions" : [ "organizations:ListOrganizationalUnitsForParent" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "organizations:TagResource", "organizations:UntagResource", "organizations:ListTagsForResource" ]
  },
  "required" : [ "Name", "ParentId" ],
  "createOnlyProperties" : [ "/properties/ParentId" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalProperties" : False
}