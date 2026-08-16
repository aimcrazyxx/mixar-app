/* SPDX-FileCopyrightText: 2026 Mixar Authors
 * SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
 *
 * SPDX-License-Identifier: GPL-3.0-or-later */

/** \file
 * \ingroup RNA
 *
 * Mixar-specific extensions to the WindowManager RNA.
 *
 * Adds the ``Window.global_areas`` collection so Python can
 * iterate global areas (topbar, statusbar). Upstream Blender
 * intentionally hides these because they're "system" areas not
 * meant to be addressed by addons, but Mixar's onboarding tour
 * needs to tag the topbar's regions for redraw from a Python
 * timer so the highlight border appears on step entry instead of
 * on cursor hover.
 *
 * Structure mirrors upstream rna_*.cc files: helper functions
 * inside ``#ifdef RNA_RUNTIME`` (compiled into Blender runtime via
 * the generated gen files including this .cc), ``RNA_def_*``
 * inside the ``#else`` branch (compiled into the makesrna binary
 * which generates the runtime code).
 *
 * The table entry for this file is registered in Mixar's overlay
 * of ``makesrna.cc`` (right after ``rna_wm.cc``). That same overlay
 * also injects an extra ``#include "rna_wm_mixar.cc"`` into the
 * generated ``rna_wm_gen.cc`` so the helper functions below are
 * visible to the auto-generated property wrappers for Window
 * (which are emitted into rna_wm_gen.cc because Window itself was
 * registered in rna_wm.cc).
 */

#include "RNA_define.hh"

#include "rna_internal.hh"

#include "DNA_screen_types.h"
#include "DNA_windowmanager_types.h"

#include "BLI_listbase.h"

#ifdef RNA_RUNTIME

namespace blender {

static void rna_Window_global_areas_begin(CollectionPropertyIterator *iter, PointerRNA *ptr)
{
  wmWindow *win = static_cast<wmWindow *>(ptr->data);
  rna_iterator_listbase_begin(iter, ptr, &win->global_areas.areabase, nullptr);
}

}  // namespace blender

#else /* RNA_RUNTIME */

#  include "rna_internal_types.hh"

namespace blender {

void RNA_def_wm_mixar(BlenderRNA *brna)
{
  /* `RNA_struct_find` is unavailable to the standalone makesrna executable.
   * Blender 5.2 stores its registration map in a C++ Map, so use the same
   * lookup form as rna_define.cc rather than the removed BLI_ghash API. */
  if (brna == nullptr) {
    return;
  }
  StructRNA *srna = brna->structs_map.lookup_default(UString("Window"), nullptr);
  if (srna == nullptr) {
    /* Window must already be registered; this runs immediately after RNA_def_wm. */
    return;
  }

  PropertyRNA *prop = RNA_def_property(srna, "global_areas", PROP_COLLECTION, PROP_NONE);
  RNA_def_property_collection_funcs(prop,
                                    "rna_Window_global_areas_begin",
                                    "rna_iterator_listbase_next",
                                    "rna_iterator_listbase_end",
                                    "rna_iterator_listbase_get",
                                    nullptr,
                                    nullptr,
                                    nullptr,
                                    nullptr);
  RNA_def_property_struct_type(prop, "Area");
  RNA_def_property_clear_flag(prop, PROP_EDITABLE);
  RNA_def_property_ui_text(prop,
                           "Global Areas",
                           "Window-global areas (topbar, statusbar). Mixar extension — "
                           "exposed so onboarding can address the topbar for redraw.");
}

}  // namespace blender

#endif /* RNA_RUNTIME */
