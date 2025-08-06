feat!: Migrate plugin to NetBox v4.0 compatibility

BREAKING CHANGE: This release drops support for NetBox versions prior to v4.0 and Python versions below 3.10.

## Major Changes

### Python & Dependencies
- Update Python support from 3.6-3.8 to 3.10-3.12
- Bump plugin version from 0.0.3 to 4.0.0
- Set minimum NetBox version requirement to 4.0.0

### Plugin Architecture
- Migrate all imports from `extras.plugins` to `netbox.plugins`
- Remove NetBox version checking logic (now v4.0+ only)
- Update template extension imports in template_content.py

### Forms & UI Components
- Remove BootstrapMixin from all form classes
- Remove button color properties from navigation menu items
- Update API serializers to inherit from NetBoxModelSerializer
- Add brief_fields support to all API serializers for brief mode

### Template Modernization
- Remove card-body wrappers around tables (embed directly in cards)
- Update panel classes to card classes for legacy templates
- Remove btn-sm classes from buttons
- Update icon classes from Glyphicon to Material Design Icons
- Fix HTML syntax error in device_type_pduconfig.html
- Consolidate template files (remove version-specific variants)

### FilterSets & API
- Update FilterSets to inherit from NetBoxModelFilterSet
- Enable API filters that were previously commented out
- Add comprehensive brief mode support for API serialization

### Code Quality
- Remove unused imports and deprecated functionality
- Simplify view logic by removing version compatibility code
- Clean up template structure and remove legacy files
- Update build system configuration for modern Python versions

## Files Modified
- pyproject.toml: Python version requirements, plugin version
- axians_netbox_pdu/__init__.py: Plugin config, imports, version
- axians_netbox_pdu/navigation.py: Button colors, imports, version logic
- axians_netbox_pdu/forms.py: BootstrapMixin removal
- axians_netbox_pdu/views.py: Template paths, version logic
- axians_netbox_pdu/filters.py: FilterSet inheritance
- axians_netbox_pdu/api/: Serializer updates, brief mode
- axians_netbox_pdu/template_content.py: Imports, version logic
- templates/: UI modernization, consolidation

## Compatibility
- ✅ NetBox v4.0+
- ✅ Python 3.10+
- ❌ NetBox < v4.0 (breaking change)
- ❌ Python < 3.10 (breaking change)

This migration follows the official NetBox v4.0 migration guide and ensures full compatibility with modern NetBox installations.