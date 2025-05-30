SCHEMA = {
  "typeName" : "AWS::AppStream::ApplicationEntitlementAssociation",
  "description" : "Resource Type definition for AWS::AppStream::ApplicationEntitlementAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-appstream.git",
  "definitions" : { },
  "properties" : {
    "StackName" : {
      "type" : "string"
    },
    "EntitlementName" : {
      "type" : "string"
    },
    "ApplicationIdentifier" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "StackName", "EntitlementName", "ApplicationIdentifier" ],
  "createOnlyProperties" : [ "/properties/StackName", "/properties/EntitlementName", "/properties/ApplicationIdentifier" ],
  "primaryIdentifier" : [ "/properties/StackName", "/properties/EntitlementName", "/properties/ApplicationIdentifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appstream:AssociateApplicationToEntitlement", "appstream:ListEntitledApplications" ]
    },
    "read" : {
      "permissions" : [ "appstream:ListEntitledApplications" ]
    },
    "delete" : {
      "permissions" : [ "appstream:DisassociateApplicationFromEntitlement", "appstream:ListEntitledApplications" ]
    }
  }
}